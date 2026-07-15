board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def display_board():
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print("---+---+---")

def check_win():
    win_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] and board[combo[1]] == board[combo[2]]:
            return True
    return False
    
def check_draw():
    for cell in board:
        if cell not in ["X", "O"]:
            return False
        
    return True

current_player = "X"
game_is_on = True

while game_is_on:
    display_board()

    while True:
        choice = input(f"Player {current_player}, choose a position(1-9): ")
        if not choice.isdigit() or not (1 <= int(choice) <= 9):
            print("Invalid input, please enter a number between 1 to 9.")
            continue

        index = int(choice) - 1

        if board[index] == "X" or board[index] == "O":
            print("That spot is already taken")
            continue

        break

    board[index] = current_player

    if check_win():
        display_board()
        print(f"Player {current_player} wins!")
        game_is_on = False

    elif game_is_on and check_draw():
        display_board()
        print("It's a Tie")
        game_is_on = False

    if game_is_on:
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"
