class Node: 
    def __init__(self, name, cost = 0):
        self.name = name
        self.children = []
        self.cost = cost
        self.total_cost = 0
        self.parent = None

    def addChild(self, child):
        self.children.append(child)
        return child

#Tìm & xoá Node có cost min
def deleteMinCost(list : list[Node]):
    min = list[0]
    
    for i in range(1, len(list)):
        if list[i].total_cost < min.total_cost:
            min = list[i]
    
    list.remove(min)

    return min

#Tìm kiếm đều giá
def ucs(initialState : Node, goalState : Node):

    frontier = [initialState]
    explored = []

    while frontier:
        state = deleteMinCost(frontier)

        explored.append(state)

        if(state == goalState):
            return explored

        for child in state.children:
            new_cost = child.cost + state.total_cost

            if child not in explored and child not in frontier:
                child.parent = state
                child.total_cost = new_cost
                frontier.append(child)
            # Cập nhật lại giá trị nếu tìm thấy đường đi tốt hơn
            elif child in frontier and new_cost < child.total_cost:
                child.parent = state
                child.total_cost = new_cost
        
    return False

def printPath(goalNode : Node):
    path = []
    while goalNode.parent != None:
        path.append(goalNode.name)
        goalNode = goalNode.parent
    path.append(goalNode.name)
    path.reverse()
    print(" -> ".join(path))

if __name__ == "__main__":

    # Khởi tạo Graph
    nodeA = Node("A", 0) # Root node
    nodeB = Node("B", 2)
    nodeC = Node("C", 1)
    nodeD = Node("D", 3)
    nodeE = Node("E", 5)
    nodeF = Node("F", 4)
    nodeG = Node("G", 6)
    nodeH = Node("H", 3)
    nodeI = Node("I", 2)
    nodeJ = Node("J", 4)
    nodeK = Node("K", 2)
    nodeL = Node("L", 1)
    nodeM = Node("M", 4)
    nodeN = Node("N", 2)
    nodeO = Node("O", 4)

    nodeA.addChild(nodeB)
    nodeA.addChild(nodeC)
    nodeA.addChild(nodeD)
    nodeB.addChild(nodeE)
    nodeB.addChild(nodeF)
    nodeC.addChild(nodeG)
    nodeC.addChild(nodeH)
    nodeD.addChild(nodeI)
    nodeD.addChild(nodeJ)
    nodeD.addChild(nodeN)
    nodeF.addChild(nodeK)
    nodeF.addChild(nodeL)
    nodeF.addChild(nodeM)
    nodeH.addChild(nodeN)
    nodeH.addChild(nodeO)

    rs = ucs(nodeA, nodeN)
    if rs: 
        print("Total Cost: " + str(rs[-1].total_cost))
        print("Path: ")
        printPath(rs[-1])
    else: 
        print("404 Not Found UCS!")