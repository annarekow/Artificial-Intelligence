from __future__ import division
from __future__ import print_function


import sys
import math
import time
import queue as Q
import resource
import collections as C
import heapq

# universal things to keep track of
nodes_expanded = 0
max_search_depth = 0
running_time = 0
state_number = 0
id_number = 0


## The Class that Represents the Puzzle
class PuzzleState(object):
    """
        The PuzzleState stores a board configuration and implements
        movement instructions to generate valid children.
    """

    def __init__(self, config, n, parent=None, action="Initial", cost=0):
        """
        :param config->List : Represents the n*n board, for e.g. [0,1,2,3,4,5,6,7,8] represents the goal state.
        :param n->int : Size of the board
        :param parent->PuzzleState
        :param action->string
        :param cost->int
        """
        if n * n != len(config) or n < 2:
            raise Exception("The length of config is not correct!")
        if set(config) != set(range(n * n)):
            raise Exception("Config contains invalid/duplicate entries : ", config)

        self.n = n
        self.cost = cost
        self.parent = parent
        self.action = action
        self.config = config
        self.children = []

        # Get the index and (row, col) of empty block
        self.blank_index = self.config.index(0)

    def display(self):
        """ Display this Puzzle state as a n*n board """
        for i in range(self.n):
            print(self.config[3 * i: 3 * (i + 1)])

    def move_up(self):
        """
        Moves the blank tile one row up.
        :return a PuzzleState with the new configuration
        """
        if self.action == 'Down':  # check for return move
            return None
        blank = self.config.index(0)
        if blank >= 3:
            new = PuzzleState(config=self.config[:], n=int(math.sqrt(len(self.config))), parent=self, cost=self.cost + 1,
                              action='Up')
            temp = new.config[blank - 3]
            new.config[blank - 3] = 0
            new.config[blank] = temp
            return new
        else:
            return None

    def move_down(self):
        """
        Moves the blank tile one row down.
        :return a PuzzleState with the new configuration
        """
        if self.action == 'Up':  # check for return move
            return None
        blank = self.config.index(0)
        if blank <= 5:
            new = PuzzleState(config=self.config[:], n=int(math.sqrt(len(self.config))), parent=self, cost=self.cost + 1,
                              action='Down')
            temp = new.config[blank + 3]
            new.config[blank + 3] = 0
            new.config[blank] = temp
            return new
        else:
            return None

    def move_left(self):
        """
        Moves the blank tile one column to the left.
        :return a PuzzleState with the new configuration
        """
        if self.action == 'Right':  # check for return move
            return None
        blank = self.config.index(0)
        if blank % 3 != 0:
            new = PuzzleState(config=self.config[:], n=int(math.sqrt(len(self.config))), parent=self, cost=self.cost + 1,
                              action='Left')
            temp = new.config[blank - 1]
            new.config[blank - 1] = 0
            new.config[blank] = temp
            return new
        else:
            return None

    def move_right(self):
        """
        Moves the blank tile one column to the right.
        :return a PuzzleState with the new configuration
        """

        if self.action == 'Left':  # check for return move
            return None
        blank = self.config.index(0)
        if blank != 2 and blank != 5 and blank != 8:
            new = PuzzleState(config=self.config[:], n=int(math.sqrt(len(self.config))), parent=self, cost=self.cost + 1,
                              action='Right')
            temp = new.config[blank + 1]
            new.config[blank + 1] = 0
            new.config[blank] = temp
            return new
        else:
            return None

    def expand(self):
        """ Generate the child nodes of this node """

        # Node has already been expanded
        if len(self.children) != 0:
            return self.children

        # increment number of nodes expanded
        global nodes_expanded
        nodes_expanded += 1

        # Add child nodes in order of UDLR
        children = [
            self.move_up(),
            self.move_down(),
            self.move_left(),
            self.move_right()]

        # Compose self.children of all non-None children states
        self.children = [state for state in children if state is not None]
        return self.children

    def expand_dfs(self):
        """ Generate the child nodes of this node """

        # Node has already been expanded
        if len(self.children) != 0:
            return self.children

        # increment number of nodes expanded
        global nodes_expanded
        nodes_expanded += 1

        # Add child nodes in order of UDLR
        children = [
            self.move_right(),
            self.move_left(),
            self.move_down(),
            self.move_up()]

        # Compose self.children of all non-None children states
        self.children = [state for state in children if state is not None]
        return self.children


# Function that Writes to output.txt

### Students need to change the method to have the corresponding parameters
def writeOutput(final_state):  # added an argument - type PuzzleState
    global nodes_expanded  # global count
    global max_search_depth  # max search depth
    global running_time  # float

    # "Floating point {0:.3f}".format(345.7916732)

    file = open('output.txt', 'w+')
    path_to_goal = []  # List of strings
    cost_of_path = final_state.cost  # cost of path
    max_ram_usage = (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)/1024
    state = final_state
    search_depth = state.cost
    while state.parent:  # populate path_to_goal
        path_to_goal.insert(0, state.action)  # prepend the action since we're moving backwards
        state = state.parent
    file.write('path_to_goal: ' + str(path_to_goal) + '\n' +
               'cost_of_path: ' + str(cost_of_path) + '\n' +
               'nodes_expanded: ' + str(nodes_expanded) + '\n' +
               'search_depth: ' + str(search_depth) + '\n' +
               'max_search_depth: ' + str(max_search_depth) + '\n' +
               'running_time: ' + str(running_time) + '\n' +
               "running_time: {0:.3f}".format(running_time) + '\n' +
               'max_ram_usage: ' + str(max_ram_usage) + '\n')


def bfs_search(initial_state):  # use an explicit queue
    """
    BFS search
    initial_state: PuzzleState -
    returns list or None
    """
    global running_time
    global max_search_depth
    start = time.time()
    frontier = Q.Queue()  # queue of objects of type PuzzleState
    frontier.put(initial_state)
    seq = convert(initial_state.config[:])
    explored = set()
    fringe = {seq}
    while not frontier.empty():
        state = frontier.get()  # next node in the frontier
        n = convert(state.config[:])  # converts config into int
        fringe.discard(n)
        explored.add(n)
        if state.cost > max_search_depth:  # added: increment max_search_depth
            max_search_depth = state.cost
        if test_goal(state.config):   # if it's the goal - return
            writeOutput(state)  # sends state to writeOutput
            end = time.time()
            running_time = (end - start)
            return state.config  # returns list
        for neighbor in state.expand():  # for each of the state's children in a list
            n_seq = convert(neighbor.config[:])
            if n_seq not in explored:
                if n_seq not in fringe: # if neighbor.config not in frontier_check or explored:  # Queue isn't iterable
                    frontier.put(neighbor)
                    fringe.add(n_seq)

    end = time.time()
    running_time = (end - start)
    return None


def dfs_search(initial_state):  # use an explicit stack
    """
    DFS search
    initial_state: PuzzleState -
    returns list or None
    """
    global running_time
    global max_search_depth
    start = time.time()
    frontier = C.deque()  # stack of objects of type PuzzleState
    frontier.append(initial_state)
    seq = convert(initial_state.config[:])  # converts list to int, e.g. start: 125340678
    explored = set()
    fringe = {seq}  # keeps track of frontier, only with config ints
    while frontier:
        state = frontier.pop()
        n = convert(state.config[:])  # converts config into int
        fringe.discard(n)  # mirrors pop for frontier
        explored.add(n)
        if state.cost > max_search_depth:
            max_search_depth = state.cost
        if test_goal(state.config):
            writeOutput(state)
            end = time.time()
            running_time = (end - start)
            return state.config  # returns list
        for neighbor in state.expand_dfs():  # expands in order RLDU
            n_seq = convert(neighbor.config[:])
            if n_seq not in explored:
                if n_seq not in fringe:
                    frontier.append(neighbor)
                    fringe.add(n_seq)

    end = time.time()
    running_time = (end - start)
    return None


class PQueue():  # version of priority queue for Astar
    def __init__(self):
        self.seqs = {}  # dictionary of {int config: total cost}
        self.states = []  # list for heap with all state info
        self.count = 0  # overall count of items pushed for comparison

    def push(self, score, node):
        self.count += 1  # increment total count
        seq = convert(node.config)  # config to int as the key in dict
        if seq in self.seqs:  # if sequence already in frontier
            if self.seqs[seq] < score:  # compare costs
                self.seqs[seq] = score  # adjust the dictionary
                heapq.heappush(self.states, [score, self.count, node.action, node])
        else:
            self.seqs[seq] = score  # add score and sequence to dictionary
            heapq.heappush(self.states, [score, self.count, node.action, node])

    def pop(self):
        while 1:
            score, count, action, node = heapq.heappop(self.states)
            seq = convert(node.config)
            if seq in self.seqs:
                del self.seqs[seq]  # delete that element from frontier
                break
            else:
                pass
        return node


def A_star_search(initial_state):  # use a priority queue
    """A * search"""
    global running_time
    global max_search_depth
    start = time.time()

    score = calculate_total_cost(initial_state)
    frontier = PQueue()
    frontier.push(score, initial_state)
    explored = set()
    while frontier.states:
        state = frontier.pop()
        explored.add(convert(state.config))  # add just the int config
        if state.cost > max_search_depth:
            max_search_depth = state.cost
        if test_goal(state.config):
            writeOutput(state)
            end = time.time()
            running_time = (end - start)
            return state.config  # returns list
        for child in state.expand():  # generate children - for each child:
            child_seq = convert(child.config)
            if child_seq not in explored:
                child_score = calculate_total_cost(child)
                frontier.push(child_score, child)  # this will take care of decreaseKey from slides pseudocode


def calculate_total_cost(state):
    """calculate the total estimated cost of a state"""
    cost = 0
    for i in range(0, len(state.config)):
        if state.config[i] != 0:
            cost += calculate_manhattan_dist(i, state.config[i], state.n)
    cost += state.cost  # total cost = cost + heuristic
    return cost


def calculate_manhattan_dist(idx, value, n):
    """
    calculate the manhattan distance of a tile
    """
    div = n  # should always be 8-puzzle, n will be 3
    if idx == value:
        return 0
    row_v, col_v = int(value/div), value % div
    row_idx, col_idx = int(idx/div), idx % div
    return abs(row_idx - row_v) + abs(col_idx - col_v)  # heuristic for single tile


def test_goal(puzzle_state_config):
    """test the state is the goal state or not"""
    if puzzle_state_config == [0, 1, 2, 3, 4, 5, 6, 7, 8]:
        return 1
    else:
        return 0


def convert(config):  # takes in config list, returns as int
    s = [str(i) for i in config]
    n = int("".join(s))
    return n


# Main Function that reads in Input and Runs corresponding Algorithm
def main():
    search_mode = sys.argv[1].lower()
    begin_state = sys.argv[2].split(",")
    begin_state = list(map(int, begin_state))
    board_size = int(math.sqrt(len(begin_state)))
    hard_state = PuzzleState(begin_state, board_size)
    start_time = time.time()

    if search_mode == "bfs":
        bfs_search(hard_state)
    elif search_mode == "dfs":
        dfs_search(hard_state)
    elif search_mode == "ast":
        A_star_search(hard_state)
    else:
        print("Enter valid command arguments !")

    end_time = time.time()
    print("Program completed in %.3f second(s)" % (end_time - start_time))


if __name__ == '__main__':
    main()
