import itertools

game_in_progress = True
game_board = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
row_length = 2
column_length = 2
current_player = 1


def display_board():
    print("")
    print("   0, 1, 2")

    for counter, row in enumerate(game_board):
        print(counter, row)
    print("")


def is_game_won():
    # print the current board
    display_board()

    # check if the game is won horizontally
    for row in game_board:
        if row.count(row[0]) == len(row) and row[0] != 0:
            print(f"Game has been won horizontally by player {current_player}")
            return True

    # check if the game is won vertically
    for col in range(len(game_board)):
        track_col = []

        for row in game_board:
            track_col.append(row[col])

        if track_col.count(track_col[0]) == len(track_col) and track_col[0] != 0:
            print(f"Game has been won vertically by player {current_player}")
            return True

    # check if the game is won diagonally
    track_diagonal = []

    for row_idx in range(len(game_board)):
        for col_idx in reversed(range(len(game_board))):
            if (row_idx + col_idx) == (len(game_board) - 1):
                track_diagonal.append(game_board[row_idx][col_idx])

    if track_diagonal.count(track_diagonal[0]) == len(track_diagonal) and track_diagonal[0] != 0:
        print(f"Game has been won diagonally by player {current_player}")
        return True

    # reset our tracker variable
    track_diagonal = []

    for idx in range(len(game_board)):
        track_diagonal.append(game_board[idx][idx])

    if track_diagonal.count(track_diagonal[0]) == len(track_diagonal) and track_diagonal[0] != 0:
        print(f"Game has been won diagonally by player {current_player}")
        return True

    # no one has won yet
    return False


def play_game():
    global game_in_progress
    # let player one take the lead
    player_cycle = itertools.cycle([1, 2])

    while game_in_progress:
        # cycle the next player to play
        global current_player
        current_player = next(player_cycle)

        # indicate which play is to play
        print(f"It is player {current_player}'s turn to play")

        # check if input is valid with a try except block
        try:
            # get user input
            column_number = int(input("Please input the column to play"))
            row_number = int(input("Please input the row to play"))

            # check if the values entered are within the ranges
            if 0 > column_number or column_number > column_length:
                print("Please input a valid number for the column")
                next(player_cycle)
                continue

            if 0 > row_number or row_number > row_length:
                print("Please input a valid number for the row")
                next(player_cycle)
                continue

            # update the game board
            game_board[row_number][column_number] = current_player

            if is_game_won():
                game_in_progress = False
        except ValueError:
            print("Please put in a valid figure")


play_game()
