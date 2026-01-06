import math
def print_board(board):
    for i in range(3):
        for j in range(3):
            print(board[i][j], end=" ")
        print()
def evaluate(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == 'X':
                return 10
            elif board[i][0] == 'O':
                return -10
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == 'X':
                return 10
            elif board[0][i] == 'O':
                return -10
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == 'X':
            return 10
        elif board[0][0] == 'O':
            return -10
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == 'X':
            return 10
        elif board[0][2] == 'O':
            return -10
    return 0
def is_moves_left(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                return True
    return False
def minimax(board, depth, is_maximizing, alpha, beta):
    score = evaluate(board)
    if score == 10:
        return score - depth
    if score == -10:
        return score + depth
    if not is_moves_left(board):
        return 0
    if is_maximizing:
        best_val = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'X'
                    best_val = max(best_val, minimax(board, depth+1, not is_maximizing, alpha, beta))
                    alpha = max(alpha, best_val)
                    board[i][j] = '_'
                    if beta <= alpha:
                        break
        return best_val
    else:
        best_val = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'O'
                    best_val = min(best_val, minimax(board, depth+1, not is_maximizing, alpha, beta))
                    beta = min(beta, best_val)
                    board[i][j] = '_'
                    if beta <= alpha:
                        break
        return best_val
def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = 'X'
                move_val = minimax(board, 0, False, -math.inf, math.inf)
                board[i][j] = '_'
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    return best_move
def main():
    board = [['_', '_', '_'],
             
             ['_', '_', '_'],
             
             ['_', '_', '_']]
        
    print("Initial Board:")
    print_board(board)
    while is_moves_left(board):
        player_move = input("Enter your move in format (row, column): ")
        row, col =map(int,player_move.split(','))
        if board[row][col] == '_':
            board[row][col] = 'O'
        else:
            print("Invalid move! Try again.")
            continue
        print_board(board)
        if not is_moves_left(board):
            break
        print("AI's move:")
        ai_move = find_best_move(board)
        board[ai_move[0]][ai_move[1]] = 'X'
        print_board(board)
    print("Game over!")
if __name__ == "__main__":    
    main()
