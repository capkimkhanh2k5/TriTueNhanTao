class Node: 
    def __init__(self, name):
        self.name = name
        self.children = []

    def addChild(self, child):
        self.children.append(child)
        return child



def bfs(initial : Node, goal : Node):

    frontier = [initial]
    explored = []

    while frontier:
        state = frontier.pop(0)

        explored.append(state)

        if(state == goal):
            return explored

        [frontier.append(child) for child in state.children if child not in (frontier and explored)]
        
    return False

def dfs(initial : Node, goal : Node):

    frontier = [initial]
    explored = []

    while frontier:
        state = frontier.pop(len(frontier) - 1)
        
        explored.append(state)

        if(state == goal):
            return explored
        
        [frontier.append(child) for child in state.children if child not in (frontier and explored)]

    
    return False

def dfs_limit(initial : Node, goal : Node, l : int):

    frontier = [initial]
    explored = []

    while frontier:
        state = frontier.pop(len(frontier) - 1)
        
        explored.append(state)

        if(state == goal):
            return explored
        
        [frontier.append(child) for child in state.children if child not in (frontier and explored)]

    
    return False

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
    rs_dfs = bfs(nodeA, nodeO) # Theo chiều rộng
    rs_bfs = dfs(nodeA, nodeO) # Theo chiều sâu

    if rs_dfs:
        print("DFS: ")
        [print(rs.name) for rs in rs_dfs]
    else: 
        print("404 Not Found DFS!")

    if rs_bfs:
        print("BFS: ")
        [print(rs.name) for rs in rs_bfs]
    else: 
        print("404 Not Found BFS!")