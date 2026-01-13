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

def DFS(initialState, goal):
    if initialState == goal:
        return [initialState], [initialState]
    
    frontier = [initialState]
    parent = {initialState: None}
    explored = set()
    order = []
    
    while frontier:
        state = frontier.pop()
        if state in explored:
            continue
        explored.add(state)
        order.append(state)
        
        if state == goal:
            path = []
            temp = state
            while temp is not None:
                path.append(temp)
                temp = parent[temp]
            path.reverse()
            return path, order
        
        neighbors = graph.get(state, [])
        for neighbor in reversed(neighbors):
            if neighbor not in explored and neighbor not in frontier:
                parent[neighbor] = state
                frontier.append(neighbor)

    return False, order

def BFS(initialState, goal):
    if initialState == goal:
        return [initialState], [initialState]
    
    frontier = [initialState]
    parent = {initialState: None}
    explored = set()
    order = []
    
    while frontier:
        state = frontier.pop(0)
        if state in explored:
            continue
        explored.add(state)
        order.append(state)
        
        if state == goal:
            path = []
            temp = state
            while temp is not None:
                path.append(temp)
                temp = parent[temp]
            path.reverse()
            return path, order
        
        for neighbor in graph.get(state, []):
            if neighbor not in explored and neighbor not in frontier:
                parent[neighbor] = state
                frontier.append(neighbor)

    return False, order


if __name__ == '__main__':
    result, dfs_order = DFS('s', 'g')
    result2, bfs_order = BFS('s', 'g')
    
    if result:
        print('DFS:', ' -> '.join(dfs_order))
        print(f"Min path:", result)
        print()
        print('BFS:', ' -> '.join(bfs_order))
        print(f"Min path:", result2)
    else:
        print("404 Not Found!")