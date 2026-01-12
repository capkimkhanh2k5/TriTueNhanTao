class Node: 
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parent = None

    def addChild(self, child: 'Node'):
        self.children.append(child)
        return child
    
    def addParent(self, nodeParent : 'Node'):
        self.parent = nodeParent

def bfs(initial : Node, goal : Node):

    frontier = [initial]
    frontier_set = {initial.name}
    explored = set()
    explored_list = []

    while frontier:
        state = frontier.pop(0)
        frontier_set.discard(state.name)

        if state.name in explored:
            continue
            
        explored.add(state.name)
        explored_list.append(state)

        if state == goal:
            return explored_list

        for child in state.children:
            if child.name not in explored and child.name not in frontier_set:
                child.addParent(state)
                frontier.append(child)
                frontier_set.add(child.name)
        
    return False

def dfs(initial : Node, goal : Node):

    frontier = [initial]
    frontier_set = {initial.name}
    explored = set()
    explored_list = []

    while frontier:
        state = frontier.pop()  # Pop từ cuối (LIFO - Stack)
        frontier_set.discard(state.name)

        if state.name in explored:
            continue
            
        explored.add(state.name)
        explored_list.append(state)
        
        if state == goal:
            return explored_list
        
        # Thêm children theo thứ tự ngược để DFS đi đúng chiều
        for child in reversed(state.children):
            if child.name not in explored and child.name not in frontier_set:
                child.addParent(state)
                frontier.append(child)  # Append (push)
                frontier_set.add(child.name)

    
    return False

def dfs_limit(initial : Node, goal : Node, l : int):

    frontier = [initial]
    frontier_set = {initial.name}
    explored = set()
    explored_list = []
    
    count = 0
    while frontier and count < l:
        count += 1

        state = frontier.pop()  # Pop từ cuối (LIFO)
        frontier_set.discard(state.name)
        
        if state.name in explored:
            continue

        explored.add(state.name)
        explored_list.append(state)

        if state == goal:
            return explored_list
        
        # Thêm children theo thứ tự ngược để DFS đi đúng chiều
        for child in reversed(state.children):
            if child.name not in explored and child.name not in frontier_set:
                child.addParent(state)
                frontier.append(child)  # Append (push)
                frontier_set.add(child.name)

    
    return False

def printPath(goalNode : Node):
    path = []
    while goalNode.parent != None:
        path.append(goalNode.name)
        goalNode = goalNode.parent
    path.append(goalNode.name)
    path.reverse()
    print(" -> ".join(path))

def printExploredPath(explored_list):
    """In thứ tự các node được visited"""
    visited_order = " -> ".join([node.name for node in explored_list])
    return visited_order

def getPath(goalNode : Node):
    """Lấy path dưới dạng list"""
    path = []
    while goalNode.parent != None:
        path.append(goalNode.name)
        goalNode = goalNode.parent
    path.append(goalNode.name)
    path.reverse()
    return path

def build_graph(graph_def: dict):
    """Khởi tạo Graph từ dictionary"""
    nodes = {}
    
    # Tạo toàn bộ node
    for parent, children in graph_def.items():
        if parent not in nodes:
            nodes[parent] = Node(parent)
        for child in children:
            if child not in nodes:
                nodes[child] = Node(child)
    
    # Gắn quan hệ cha-con (directed)
    for parent, children in graph_def.items():
        for child in children:
            nodes[parent].addChild(nodes[child])
    
    return nodes

if __name__ == "__main__":

    graph = {
        'a' : ['b', 'c'],
        'b' : ['d', 'a'],
        'c' : ['h', 'a'],
        'd' : ['e', 'k', 'b'],
        'e' : ['m', 'd'],
        'h' : ['s', 'c'],
        'k' : ['m', 't', 'd'],
        'f' : ['s', 'p'],
        'g' : ['t', 'm'],
        's' : ['h', 'f'],
        'm' : ['n', 'g', 'k', 'e'],
        'n' : ['m'],
        't' : ['g', 'r', 'k'],
        'r' : ['t', 'q'],
        'q' : ['r', 'p'],
        'p' : ['q', 'f'],
    }

    # Khởi tạo Graph từ dictionary
    nodes = build_graph(graph)

    # Reset parent
    for node in nodes.values():
        node.parent = None

    # Chạy DFS trước
    rs_dfs = dfs(nodes['s'], nodes['g'])
    
    # Reset parent
    for node in nodes.values():
        node.parent = None
    
    # Chạy BFS
    rs_bfs = bfs(nodes['s'], nodes['g'])

    if rs_dfs:
        dfs_explored = " -> ".join([node.name for node in rs_dfs])
        print("DFS:", dfs_explored)
        # Min path là từ explored list cuối cùng (goal) duyệt ngược lại start
        min_path = [rs_dfs[-1].name]
        current = rs_dfs[-1]
        for node in reversed(rs_dfs[:-1]):
            if current.name in [child.name for child in node.children]:
                min_path.insert(0, node.name)
                current = node
        print("Min path:", min_path)
    else: 
        print("404 Not Found DFS!")

    print()

    if rs_bfs:
        print("BFS:", printExploredPath(rs_bfs))
        print("BFS path from 's' to 'g':", getPath(rs_bfs[-1]))
    else: 
        print("404 Not Found BFS!")

    # Reset parent
    for node in nodes.values():
        node.parent = None

    L = 2
    rs_bfsLimit = dfs_limit(nodes['a'], nodes['n'], L)

    if rs_bfsLimit:
        print("DFS Limit with L = " + str(L) + " :")
        print("Path: ")
        printPath(rs_bfsLimit[-1])
    else: 
        print("404 Not Found DFS Limit with L = " + str(L) + "!")
