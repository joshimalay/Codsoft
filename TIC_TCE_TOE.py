import math
 # The Tic-Tac-Toe board
board = [' ' for _ in range(9)]
def print_board():
    print()
    for row in [board[i * 3:(i + 1) * 3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')
def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # vertical
        [0, 4, 8], [2, 4, 6]              # diagonal
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False
def is_board_full(board):
    return ' ' not in board
def minimax(board, depth, is_maximizing):
    if check_winner(board, 'O'):
        return 1
    elif check_winner(board, 'X'):
        return -1
    elif is_board_full(board):
        return 0
    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score
def ai_move():
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    board[move] = 'O'
def human_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] == ' ':
                board[move] = 'X'
                break
            else:
                print("This spot is taken!")
        except (IndexError, ValueError):
            print("Invalid move. Please try again.")
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board()
    while True:
        human_move()
        print_board()
        if check_winner(board, 'X'):
            print("You win!")
            break
        if is_board_full(board):
            print("It's a tie!")
            break
        ai_move()
        print_board()
        if check_winner(board, 'O'):
            print("You lose!")
            break
        if is_board_full(board):
            print("It's a tie!")
            break
if __name__ == "__main__":
    play_game()
    


