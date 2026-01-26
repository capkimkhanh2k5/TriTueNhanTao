# =========================
# TreeNode / Tree definition
# =========================

class Tree:
    def __init__(self, name):
        self.name = name
        self.value = None
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __repr__(self):
        return f"Tree({self.name}, value={self.value})"


# =========================
# Alpha-Beta Pruning
# =========================

def MaxValue(node, alpha, beta):
    # Leaf node
    if len(node.children) == 0:
        return node

    node.value = -100000

    for child in node.children:
        temp = MinValue(child, alpha, beta)

        if temp.value > node.value:
            node.value = temp.value

        # Beta cutoff
        if child.value >= beta:
            return child

        if child.value > alpha:
            alpha = child.value

    return node


def MinValue(node, alpha, beta):
    # Leaf node
    if len(node.children) == 0:
        return node

    node.value = 100000

    for child in node.children:
        temp = MaxValue(child, alpha, beta)

        if temp.value < node.value:
            node.value = temp.value

        # Alpha cutoff
        if child.value <= alpha:
            return child

        if child.value < beta:
            beta = child.value

    return node


def Alpha_Beta_Search(state):
    return MaxValue(state, -100000, 100000)


# =========================
# Main
# =========================

if __name__ == "__main__":
    A = Tree("A")
    B = Tree("B")
    C = Tree("C")
    D = Tree("D")
    E = Tree("E")
    F = Tree("F")
    G = Tree("G")
    H = Tree("H")
    I = Tree("I")
    J = Tree("J")
    K = Tree("K")
    L = Tree("L")
    M = Tree("M")
    N = Tree("N")
    Z = Tree("Z")

    A.add_child(B)
    A.add_child(C)

    B.add_child(D)
    B.add_child(E)

    C.add_child(F)
    C.add_child(G)

    D.add_child(H)
    D.add_child(I)

    E.add_child(J)
    E.add_child(K)

    F.add_child(M)
    F.add_child(N)

    G.add_child(L)
    G.add_child(Z)

    # Leaf values
    H.value = 2
    I.value = 9
    J.value = 7
    K.value = 4
    M.value = 8
    N.value = 9
    L.value = 3
    Z.value = 5

    Alpha_Beta_Search(A)

    print("Giá trị tại nút gốc A:", A.value)
