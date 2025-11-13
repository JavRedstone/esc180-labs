# QUESTION 5
'''
 X | O | X
---+---+---
 O | O | X
---+---+---
   | X |
'''

import random


def print_board_and_legend(board):
    for i in range(3):
        line1 = " " +  board[i][0] + " | " + board[i][1] + " | " +  board[i][2]
        line2 = "  " + str(3*i+1)  + " | " + str(3*i+2)  + " | " +  str(3*i+3)
        print(line1 + " "*5 + line2)
        if i < 2:
            print("---+---+---" + " "*5 + "---+---+---")

def make_empty_board():
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board

# QUESTION 5a)
def get_coord(square_num):
    r = (square_num - 1) // 3
    c = (square_num - 1) % 3
    return [r, c]

# QUESTION 5b)
def put_in_board(board, mark, square_num):
    r, c = get_coord(square_num)
    board[r][c] = mark

# QUESTION 5c)
def player_play(board, is_X):
    while True:
        mark = 'X' if is_X else 'O'
        square_num = int(input(f"Enter square number for {mark}: "))
        if square_num not in range(1, 10):
            print("YOU QUIT")
            return

        tried_to_cheat = False
        if get_coord(square_num) not in get_free_squares(board):
            tried_to_cheat = True
            print("You cannot place a mark in an already occupied cell")
        else:
            put_in_board(board, mark, square_num)

        if not tried_to_cheat:
            is_X = not is_X

        print_board_and_legend(board)

        if len(get_free_squares(board)) == 0:
            print("It's a DRAW!")
            return

# QUESTION 6a)
def get_free_squares(board):
    free = []
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == ' ':
                free.append([r, c])
    return free

# QUESTION 6b)
def make_random_move(board, mark):
    free = get_free_squares(board)
    if len(free) == 0:
        return
    rand_free = free[int(len(free) * random.random())]
    board[rand_free[0]][rand_free[1]] = mark

# QUESTION 7a)
def is_row_all_marks(board, row_i, mark):
    return board[row_i] == [mark] * len(board[row_i])

# QUESTION 7b)
def is_col_all_marks(board, col_i, mark):
    for r in range(len(board)):
        if board[r][col_i] != mark:
            return False
    return True

# QUESTION 7c)
def is_diag_all_marks(board, is_back, mark):
    for r in range(len(board)):
        c = r if is_back else len(board[r]) - r - 1
        if board[r][c] != mark:
            return False
    return True

def is_win(board, mark):
    for r in range(len(board)):
        if is_row_all_marks(board, r, mark):
            return True
    for c in range(len(board[0])):
        if is_col_all_marks(board, c, mark):
            return True
    if is_diag_all_marks(board, True, mark):
        return True
    if is_diag_all_marks(board, False, mark):
        return True
    return False

# QUESTION 7d)
def player_play_win(board, is_X):
    while True:
        mark = 'X' if is_X else 'O'
        square_num = int(input(f"Enter square number for {mark}: "))
        if square_num not in range(1, 10):
            print("YOU QUIT")
            return

        tried_to_cheat = False
        if get_coord(square_num) not in get_free_squares(board):
            tried_to_cheat = True
            print("You cannot place a mark in an already occupied cell")
        else:
            put_in_board(board, mark, square_num)

        if is_win(board, mark):
            print(f"Player with mark {mark} wins the game!")
            return

        if not tried_to_cheat:
            is_X = not is_X
        print_board_and_legend(board)

        if len(get_free_squares(board)) == 0:
            print("It's a DRAW!")
            return

def player_comp_play_win(board, make_comp_move, is_X):
    while True:
        mark = 'X' if is_X else 'O'
        square_num = int(input(f"Enter square number for {mark}: "))
        if square_num not in range(1, 10):
            print("YOU QUIT")
            break

        tried_to_cheat = False
        if get_coord(square_num) not in get_free_squares(board):
            tried_to_cheat = True
            print("You cannot place a mark in an already occupied cell")
        else:
            put_in_board(board, mark, square_num)

        print_board_and_legend(board)

        if tried_to_cheat:
            continue

        if is_win(board, mark):
            print(f"You with mark {mark} win the game!")
            return
        print("Computer move: ===================")
        comp_mark = 'O' if mark == 'X' else 'X'
        make_comp_move(board, comp_mark)
        if is_win(board, comp_mark):
            print(f"Computer with mark {comp_mark} wins the game!")
            return
        print_board_and_legend(board)

        if len(get_free_squares(board)) == 0:
            print("It's a DRAW!")
            return

# QUESTION 8a)
def make_slightly_smarter_move(board, mark):
    free = get_free_squares(board)
    for r, c in free:
        board[r][c] = mark
        if is_win(board, mark):
            return
        else:
            board[r][c] = " "
    make_random_move(board, mark)

# QUESTION 8b)
def make_big_brain_move(board, mark):
    free = get_free_squares(board)
    # Either computer wins directly
    for r, c in free:
        board[r][c] = mark
        if is_win(board, mark):
            return
        else:
            board[r][c] = " "
    # Or computer blocks off the player's next move
    player_mark = 'O' if mark == 'X' else 'X'
    for r, c in free:
        board[r][c] = player_mark
        if is_win(board, player_mark):
            board[r][c] = mark
            return
        else:
            board[r][c] = " "
    # Or computer takes center position
    if [1, 1] in free:
        board[1][1] = mark
        return

    make_random_move(board, mark)

if __name__ == '__main__':
    board = make_empty_board()
    print_board_and_legend(board)

    print("\n\n")

    board = [["O", "X", "X"],
             [" ", "X", " "],
             [" ", "O", " "]]

    print_board_and_legend(board)

    # QUESTION 5a)
    print("QUESTION 5a) --------------------")
    coord = get_coord(8)
    print(f"Coord: r = {coord[0]}, c = {coord[1]}. Board: {board[coord[0]][coord[1]]}")

    # QUESTION 5b)
    print("QUESTION 5b) --------------------")
    put_in_board(board, "O", 4)
    print_board_and_legend(board)

    # QUESTION 5c)
    print("QUESTION 5c) --------------------")
    player_play(board, True)

    # QUESTION 6a)
    print("QUESTION 6a) --------------------")
    print_board_and_legend(board)
    free = get_free_squares(board)
    print(free)

    # QUESTION 6b)
    print("QUESTION 6b) --------------------")
    print_board_and_legend(board)
    make_random_move(board, 'X')
    print_board_and_legend(board)

    # QUESTION 7a)
    print("QUESTION 7a) --------------------")
    print_board_and_legend(board)
    print(is_row_all_marks(board, 0, 'X'))

    # QUESTION 7b)
    print("QUESTION 7b) --------------------")
    print_board_and_legend(board)
    print(is_col_all_marks(board, 1, 'X'))

    # QUESTION 7c)
    print("QUESTION 7c) --------------------")
    print_board_and_legend(board)
    print(is_win(board, 'X'))

    # QUESTION 7d)
    print("QUESTION 7d) --------------------")
    board = make_empty_board()
    print_board_and_legend(board)
    player_play_win(board, True)
    print_board_and_legend(board)

    board = make_empty_board()
    print_board_and_legend(board)
    player_comp_play_win(board, make_random_move, True)
    print_board_and_legend(board)

    # QUESTION 8a)
    print("QUESTION 8a) --------------------")
    board = make_empty_board()
    print_board_and_legend(board)
    player_comp_play_win(board, make_slightly_smarter_move, True)
    print_board_and_legend(board)

    # QUESTION 8b)
    print("QUESTION 8b) --------------------")
    board = make_empty_board()
    print_board_and_legend(board)
    player_comp_play_win(board, make_big_brain_move, True)
    print_board_and_legend(board)
