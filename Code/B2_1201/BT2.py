class Node: 
    def __init__(self, name, x=0, y=0, cost=0):
        self.name = name
        self.x = x
        self.y = y
        self.children = []
        self.cost = cost  # Chi phí cạnh
        self.g = 0  # Chi phí từ nút bắt đầu (accumulated)
        self.parent = None

    def addChild(self, child):
        self.children.append(child)
        return child

#Tìm & xoá Node có chi phí g(x) nhỏ nhất
def deleteMinCost(frontier: list):
    min_node = frontier[0]
    
    for node in frontier[1:]:
        if node.g < min_node.g:
            min_node = node
    
    frontier.remove(min_node)
    return min_node

#Hàm chi phí đích đến - manhattan distance từ (x,y) đến (5,4)
def cost(x, y):
    return abs(x - 5) + abs(y - 4)

#Tìm kiếm đều giá
def ucs(initialState: Node, goalState: Node):
    frontier = [initialState]
    frontier_set = {initialState.name}
    explored = set()

    while frontier:
        state = deleteMinCost(frontier)
        frontier_set.discard(state.name)
        explored.add(state.name)

        if state == goalState:
            return state

        for child in state.children:
            new_cost = state.g + cost(child.x, child.y)

            if child.name not in explored and child.name not in frontier_set:
                child.parent = state
                child.g = new_cost
                frontier.append(child)
                frontier_set.add(child.name)
            # Cập nhật lại giá trị nếu tìm thấy đường đi tốt hơn
            elif child.name in frontier_set and new_cost < child.g:
                child.parent = state
                child.g = new_cost
        
    return False

def printPath(goalNode: Node):
    path = []
    while goalNode.parent != None:
        path.append(goalNode.name)
        goalNode = goalNode.parent
    path.append(goalNode.name)
    path.reverse()
    print(" -> ".join(path))

if __name__ == "__main__":

    # Định nghĩa Graph
    graph = {
        ('a', 3, 1): ['b', 'c'],
        ('b', 4, 1): ['d', 'a'],
        ('c', 3, 2): ['h', 'a'],
        ('d', 4, 2): ['e', 'k', 'b'],
        ('e', 5, 2): ['m', 'd'],
        ('h', 3, 3): ['s', 'c'],
        ('k', 4, 3): ['m', 't', 'd'],
        ('f', 1, 3): ['s', 'p'],
        ('g', 2, 4): ['t', 'm'],
        ('s', 2, 3): ['h', 'f'],
        ('m', 5, 3): ['n', 'g', 'k', 'e'],
        ('n', 6, 3): ['m'],
        ('t', 4, 4): ['g', 'r', 'k'],
        ('r', 3, 4): ['t', 'q'],
        ('q', 3, 4): ['r', 'p'],
        ('p', 1, 4): ['q', 'f'],
    }

    # Xây dựng các Node từ graph
    nodes = {}
    for (name, x, y), neighbors in graph.items():
        if name not in nodes:
            nodes[name] = Node(name, x, y)
    
    # Gắn quan hệ parent-child
    for (name, x, y), neighbors in graph.items():
        for neighbor_name in neighbors:
            nodes[name].addChild(nodes[neighbor_name])
    
    # Chạy UCS từ 's' đến 'g'
    rs = ucs(nodes['s'], nodes['g'])
    
    if rs: 
        print("Total Cost: " + str(rs.g))
        print("Path: ")
        printPath(rs)
    else: 
        print("404 Not Found UCS!")