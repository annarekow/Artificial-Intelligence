"""
Each sudoku board is represented as a dictionary with string keys and
int values.
e.g. my_board['A1'] = 8
"""
from collections import OrderedDict
# import queue as Q
import copy

ROW = "ABCDEFGHI"
COL = "123456789"
#forward_checker = {}
rows = {0: ['A', 'B', 'C'], 1: ['D', 'E', 'F'], 2: ['G', 'H', 'I']}
cols = {0: [1, 2, 3], 1: [4, 5, 6], 2: [7, 8, 9]}
# one_left = []  # tracks values that need to convert from forward_checker to assigned val


def print_board(board):
    """Helper function to print board in a square."""
    # if board == 0:
        # print('Reached wrong board')
    print("-----------------")
    for i in ROW:
        row = ''
        for j in COL:
            # print(str(board[i + j]))  ## ADDED
            row += (str(board[i + j]) + " ")
        print(row)


def board_to_string(board):
    """Helper function to convert board dictionary to string for writing."""
    ordered_vals = []
    for r in ROW:
        for c in COL:
            ordered_vals.append(str(board[r + c]))
    return ''.join(ordered_vals)


def construct(board):
    """ construct dictionary of only empty squares and their potential values """
    forward_checker = {}
    # forward_checker.clear()  # empty dictionary
    for key in board:
        if board[key] == 0:
            forward_checker[key] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # else:
            # forward_checker[key] = [board[key]]
    return forward_checker


#########
def preprocess(board, forward_checker):
    """ preprocessing step to eliminate potential values on forward_checker dict """
    # for first 0 in the board and in forward_checker
    # proceed = True
    # for element in forward_checker:
    for element in board:
        if board[element] == 0:
            # if board[element] == 0:  # or for forward_checker
            # iterate through each number in its list in forward_checkr
            # for i in range(len(forward_checker[element])):  # iterate through potentials
            for i in forward_checker[element]:
                if num_present(element, i, board):
                    forward_checker[element].remove(i)  # remove from list
            if not check(element, board, forward_checker):
                return False # checks if one element left in any list
            if element in forward_checker and len(forward_checker[element]) == 0:
                return False

        #########
    # adjust(forward_checker)  # clears up elements with only one option
    return True


#def adjust(forward_checker):
#    while len(one_left) > 0:  # one left in forward_checker
#        key = one_left.pop()
#        if key in forward_checker and len(forward_checker[key]) > 0:
#            board[key] = forward_checker[key][0]
#            clear_board(key, forward_checker[key][0], forward_checker)  # might make this return t/f
#            forward_checker.pop(key)


def check(key, board, checker):
    """ checks a single key in checker dictionary """
    valid = True  # meaning carry on
    if len(checker[key]) == 1:  # if one element left
        board[key] = checker[key][0]  # change on actual board
        valid = clear_board(key, checker[key][0], checker)  # returns false if the config doesn't work
        checker.pop(key)  # remove from forward_checker
    return valid  # if false, it means clear_board didn't work


def next_empty(checker):  # checker is dictionary
    """ returns next empty slot using minimum remaining value heuristic """
    min_len = 100  # arbitrary large assignment
    position = ' '
    values = []
    for element in checker:
        if len(checker[element]) < min_len:
            min_len = len(checker[element])
            position = element
            values = checker[element]
    return position, values


def backtracking(board, checker):
    # checker = construct(board)  # construct new checker dict based on blanks in board
    preprocess(board, checker)  # if we can preprocess without messing with heuristics
    print("new board:")  ######
    print_board(board)
    backtracker(board, checker)
    # return new_board


def backtracker(board, checker):
    """Takes a board and returns solved board."""
    # if element == ' ':  # or if element == 0
        # return board  # board is solved
    if finished_board(board):
        return board
    element, values = next_empty(checker)  # e.g. 'A1'
    for i in values:  # for all valid assignments in dict
        if not num_present(element, i, board):  # returns FALSE if i is valid
            board[element] = i  # fill in the blank
            if clear_board(element, i, checker):  # clear the potential values
                print("in inner if")
                new_check = copy.deepcopy(checker)  # copy dictionary
                new_check.pop(element)  # clear from dict of unassigned values
                new_board = copy.deepcopy(board)
                backtracking(new_board, new_check)  # begin recursion
            board[element] = 0  # go on with current board

    if finished_board(board):
        return board


##########
def finished_board(board):  # checks if board is finished
    for element in board:
        if board[element] == 0:
            return False
    return True


# GIVEN POSITION AND BOARD, IS BOARD VALID? WE USE NUM_PRESENT
def num_present(key, value, board):
    """ checks for matching values in box, column, and row """
    row, col = find_box(key)  # checks for box
    for x in rows[row]:
        for y in cols[col]:
            if str(x + str(y)) != key and board[x + str(y)] == value:
                return True
    # checks for column
    for x in ROW:
        if str(x + str(key[1])) != key and board[x + str(key[1])] == value:
            return True
    # checks for row
    for i in COL:
        if str(key[0] + str(i)) != key and board[key[0] + str(i)] == value:
            return True
    return False


def find_box(key):
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


def clear_board(key, value, checker):
    """ helper function for preprocessing step """
    # one_left.clear()  # clears list every time it checks
    row, col = find_box(key)  # checks for box
    for x in rows[row]:
        for y in cols[col]:
            # print(checker[x + str(y)])  # TODO delete later!
            # print(value)
            # print("hi")
            if str(x + str(y)) in checker:  # if this element is 0 ###

                if value in checker[x + str(y)] and str(x + str(y)) != key:
                    checker[x + str(y)].remove(value)  # remove value from list
                # if len(checker[x + str(y)]) == 1:  # if one element left
                    # one_left.append(x + str(y))  # only relevant for preprocessing
                if len(checker[x + str(y)]) == 0:  # if this is invalid board
                    return False
    for x in ROW:  # checks for column
        if str(x + str(key[1])) in checker:
            if str(x + str(key[1])) != key and value in checker[x + str(key[1])]:  # board[x + str(key[1])] == value:
                # if len(checker[x + str(key[1])]) > 0:
                checker[x + str(key[1])].remove(value)
            # if len(checker[x + str(key[1])]) == 1:  # if one element left
                # one_left.append(x + str(key[1]))
            if len(checker[x + str(key[1])]) == 0:  # if this is invalid board
                return False
    for i in COL:  # checks for row
        if str(key[0] + str(i)) in checker:
            if str(key[0] + str(i)) != key:
                if value in checker[key[0] + str(i)]:  # board[key[0] + str(i)] == value:
                # if len(checker[key[0] + str(i)]) > 0:
                    # print('value:')  ##
                    # print(value)  ##
                    # print('array:')  ##
                    # print(checker[key[0] + str(i)])
                    checker[key[0] + str(i)].remove(value)
            # if len(checker[key[0] + str(i)]) == 1:  # if one element left
                # one_left.append(key[0] + str(i))
            if len(checker[key[0] + str(i)]) == 0:  # if this is invalid board
                return False
    # return False
    # adjust(checker)  #####
    return True  # then the new heuristics work!!

# clear square/row/column of constraints if a number is written on board


if __name__ == '__main__':
    #  Read boards from source.
    src_filename = 'sudokus_start.txt'
    try:
        srcfile = open(src_filename, "r")
        sudoku_list = srcfile.read()
    except:
        print("Error reading the sudoku file %s" % src_filename)
        exit()

    # Setup output file
    out_filename = 'output.txt'
    outfile = open(out_filename, "w")

    # Solve each board using backtracking
    for line in sudoku_list.split("\n"):

        if len(line) < 9:
            continue

        # Parse boards to dict representation, scanning board L to R, Up to Down
        board = { ROW[r] + COL[c]: int(line[9*r+c])
                  for r in range(9) for c in range(9)}

        # Print starting board. TODO: Comment this out when timing runs.
        # print_board(board)

        ## ADDED PREPROCESSING FUNCTION
        checker = construct(board)
        # preprocess(board)
        ##

        # Solve with backtracking
        solved_board = backtracking(board, checker)

        # Print solved board. TODO: Comment this out when timing runs.
        if solved_board:  ###### ADDED
            print("Found solved board!")  #####  ADDED
            print_board(solved_board)

            # Write board to file
            outfile.write(board_to_string(solved_board))
            outfile.write('\n')

    print("Finishing all boards in file.")
