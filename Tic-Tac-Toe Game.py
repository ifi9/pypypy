# Initialize the board
board = [" " for _ in range(9)]

# Function to print the board
def print_board():
    for i in range(0, 9, 3):
        print(board[i] + "|" + board[i+1] + "|" + board[i+2])
        if i < 6:
            print("-+-+-")

# Function to check for a win
def check_win(player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
                      (0, 4, 8), (2, 4, 6)]            # Diagonals
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)

# Function to play the game
def play_game():
    current_player = "X"
    
    while " " in board:
        print_board()
        move = int(input(f"Player {current_player}, choose a position (1-9): ")) - 1
        
        if board[move] == " ":
            board[move] = current_player
            if check_win(current_player):
                print_board()
                print(f"Player {current_player} wins!")
                return
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Position taken, try again.")
    
    print_board()
    print("It's a draw!")

# Run the game
play_game()
