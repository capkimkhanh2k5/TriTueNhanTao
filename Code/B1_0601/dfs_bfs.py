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
    explored = []

    while frontier:
        state = frontier.pop(0)

        explored.append(state)

        if(state == goal):
            return explored

        for child in state.children:
            if child not in frontier and child not in explored:
                child.addParent(state)
                frontier.append(child)
        
    return False

def dfs(initial : Node, goal : Node):

    frontier = [initial]
    explored = []

    while frontier:
        state = frontier.pop(len(frontier) - 1)
        
        explored.append(state)

        if(state == goal):
            return explored
        
        for child in state.children:
            if child not in frontier and child not in explored:
                child.addParent(state)
                frontier.append(child)

    
    return False

def dfs_limit(initial : Node, goal : Node, l : int):

    frontier = [initial]
    explored = []
    
    count = 0
    while frontier and count < l:
        count += 1

        state = frontier.pop(len(frontier) - 1)
        
        explored.append(state)

        if(state == goal):
            return explored
        
        for child in state.children:
            if child not in frontier and child not in explored:
                child.addParent(state)
                frontier.append(child)

    
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
    nodeA = Node("A") # Root node
    nodeB = Node("B")
    nodeC = Node("C")
    nodeD = Node("D")
    nodeE = Node("E")
    nodeF = Node("F")
    nodeG = Node("G")
    nodeH = Node("H")
    nodeI = Node("I")
    nodeJ = Node("J")
    nodeK = Node("K")
    nodeL = Node("L")
    nodeM = Node("M")
    nodeN = Node("N")
    nodeO = Node("O")

    nodeA.addChild(nodeB)
    nodeA.addChild(nodeC)
    nodeB.addChild(nodeD)
    nodeB.addChild(nodeE)
    nodeC.addChild(nodeF)
    nodeC.addChild(nodeG)
    nodeD.addChild(nodeH)
    nodeD.addChild(nodeI)
    nodeE.addChild(nodeJ)
    nodeE.addChild(nodeK)
    nodeF.addChild(nodeL)
    nodeF.addChild(nodeM)
    nodeG.addChild(nodeN)
    nodeG.addChild(nodeO)

    # Tìm kiếm
    rs_dfs = bfs(nodeA, nodeM) # Theo chiều rộng
    rs_bfs = dfs(nodeA, nodeM) # Theo chiều sâu

    if rs_dfs:
        print("BFS: ")
        printPath(rs_dfs[-1])
    else: 
        print("404 Not Found BFS!")

    if rs_bfs:
        print("DFS: ")
        printPath(rs_bfs[-1])
    else: 
        print("404 Not Found DFS!")

    L = 2
    rs_bfsLimit = dfs_limit(nodeA, nodeO, L)

    if rs_bfsLimit:
        print("DFS Limit with L = " + str(L) + " :")
        print("Path: ")
        printPath(rs_bfsLimit[-1])
    else: 
        print("404 Not Found DFS Limit with L = " + str(L) + "!")