#!/usr/bin/env python
#coding:utf-8

"""
Each sudoku board is represented as a dictionary with string keys and
int values.
e.g. my_board['A1'] = 8
"""
import copy
import time
import statistics as s
import sys

ROW = "ABCDEFGHI"
COL = "123456789"
rows = {0: ['A', 'B', 'C'], 1: ['D', 'E', 'F'], 2: ['G', 'H', 'I']}
cols = {0: [1, 2, 3], 1: [4, 5, 6], 2: [7, 8, 9]}


def print_board(board):
    """Helper function to print board in a square."""
    if board:
        print("-----------------")
        for i in ROW:
            row = ''
            for j in COL:
                row += (str(board[i + j]) + " ")
            print(row)


def board_to_string(board):
    """Helper function to convert board dictionary to string for writing."""
    if board:  ###
        ordered_vals = []
        for r in ROW:
            for c in COL:
                ordered_vals.append(str(board[r + c]))
        return ''.join(ordered_vals)


def backtracking(sudoku_board):
    """Takes a board from INPUT and returns solved board."""
    heuristics = generate_h(sudoku_board)  # generate heuristics
    return backtrack(sudoku_board, heuristics)


def preprocess(board, heuristics):
    """ preprocesses each new board before attempting backtracking """
    while True:
        # print('in pre!')
        key = select_unassigned_variable(heuristics)
        if len(heuristics[key]) == 1:
            board[key] = heuristics[key][0]
            clear_h(board, heuristics)
        else:
            break
    if finished(board):
        print('finished in preprocess!')


def backtrack(board, heuristics):
    """ internal backtracking function """
    if finished(board):  # if no blanks left
        return board
    blank = select_unassigned_variable(heuristics)
    for i in heuristics[blank]:  # order_domain_values is not a function
        board[blank] = i
        new_heur = copy.deepcopy(heuristics)
        new_heur.pop(blank)  # remove element from dict of blanks
        if clear_h(board, new_heur):  # forward check
            new = backtrack(board, new_heur)  ## ???
            if finished(new):
                return new
        board[blank] = 0


def finished(board):
    if board:
        valid = True
        for key in board:
            if board[key] == 0:
                valid = False
        return valid


def select_unassigned_variable(heuristics):
    """ selects next blank to fill, returns its position """
    min_len = 100  # arbitrary large assignment
    position = ''
    for key in heuristics:
        if len(heuristics[key]) == 1:
            position = key
            return position
        if len(heuristics[key]) < min_len:
            min_len = len(heuristics[key])
            position = key
    return position


def generate_h(board):
    """ generates a new heuristic for a new board from input file """
    heuristics = {}
    for key in board:
        if board[key] == 0:
            heuristics[key] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    clear_h(board, heuristics)  # will return true/false, but not expecting invalid boards
    return heuristics


def clear_h(board, heuristics):
    """ clears heuristics list of interfering elements that exist on board """
    """ returns true if each heuristic has at least one element """
    for key in board:
        if board[key] == 0:
            for i in heuristics[key]:  # for element in list
                if num_present(key, i, board):  # if board has interfering element
                    heuristics[key].remove(i)  # clear from heurisitics
            if len(heuristics[key]) == 0:
                return False
    return True


def num_present(key, value, board):
    """ checks for matching values in box, column, and row """
    global rows, cols
    row, col = find_box(key)  # checks for box
    for x in rows[row]:
        for y in cols[col]:
            if str(x + str(y)) != key and board[x + str(y)] == value:
                return True
    for x in ROW:  # checks for column
        if str(x + str(key[1])) != key and board[x + str(key[1])] == value:
            return True
    for i in COL:  # checks for row
        if str(key[0] + str(i)) != key and board[key[0] + str(i)] == value:
            return True
    return False


def find_box(key):
    """ locates the box of a given element """
    row, col = 0, 0  # start at A1
    for i in range(9):
        if ROW[i] == key[0]:
            row = i // 3  # ABC = 0, DEF = 1, GHI = 2
            break
    for i in range(9):
        if COL[i] == key[1]:
            col = i // 3  # 123 = 0, 456 = 1, 789 = 2
            break
    return row, col


if __name__ == '__main__':
    #  Read boards from source.
    # src_filename = 'sudokus_start.txt'
    # try:
        # srcfile = open(src_filename, "r")
        # sudoku_list = srcfile.read()
        # line = str(sys.argv)
    # except:
        # print("Error reading the sudoku file %s" % src_filename)
        # print('Error reading input board')
        # exit()

    # Setup output file
    out_filename = 'output.txt'
    outfile = open(out_filename, "w")

    # ADDED: TIME TRACKING
    # times = []
    # max_time = -100
    # min_time = 200
    # count = 0
    line = sys.argv[1]
    # print(line)  ###

    # Solve each board using backtracking
    # for line in sudoku_list.split("\n"):

    # if len(line) < 9:
        # continue

    # Parse boards to dict representation, scanning board L to R, Up to Down
    board = { ROW[r] + COL[c]: int(line[9*r+c])
        for r in range(9) for c in range(9)}

    # Print starting board. TODO: Comment this out when timing runs.
    # print_board(board)

    # Solve with backtracking
    start = time.time()  ###
    solved_board = backtracking(board)

    # Print solved board. TODO: Comment this out when timing runs.
    print_board(solved_board)

    # Write board to file
    outfile.write(board_to_string(solved_board))
    outfile.write('\n')
    end = time.time()  ###
    # count += 1

    # Calculate times
    # t = end - start
    # times.append(t)
    # if t > max_time:
        # max_time = t
    # elif t < min_time:
        # min_time = t

    # print("Finishing all boards in file.")

    # More time calculation
    # std = s.stdev(times)
    # mean = s.mean(times)
    ### print mean std max and min!!! then write README
    # print('std: ' + str(std) + 'mean: ' + str(mean))
    # print('max: ' + str(max_time) + 'min ' + str(min_time))
    # print('boards solved: ' + str(count))
