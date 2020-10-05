"""
<Anna Rekow>
"""


import numpy as np


def p1(k: int) -> str:
    n = k
    arr = []
    # no check for negatives
    for i in range(1, n+1):
        x = p1_fact(i)
        arr.append(x)
    arr.reverse()
    return str(arr)[1:-1]


def p1_fact(k: int) -> int:
    # helper factorial function for p1
    n = k
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact


def p2_a(x: list, y: list) -> list:
    d = y.copy()
    d.sort(reverse=True)
    d.pop()
    return d


def p2_b(x: list, y: list) -> list:
    d = x.copy()
    d.reverse()
    return d


def p2_c(x: list, y: list) -> list:
    return list(set(x.copy() + y.copy()))


def p2_d(x: list, y: list) -> list:
    d = [x.copy(), y.copy()]
    return d


def p3_a(x: set, y: set, z: set) -> set:
    return x.copy().union(y.copy(), z.copy())


def p3_b(x: set, y: set, z: set) -> set:
    return x.copy().intersection(y.copy(), z.copy())


def p3_c(x: set, y: set, z: set) -> set:
    b = (x.copy() - y.copy() - z.copy()).union(y.copy() - z.copy() - x.copy()).union(z.copy() - x.copy() - y.copy())
    return b


def p4_a() -> np.array:
    a = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 2, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]
    npa = np.array(a)
    return npa


def p4_b(x: np.array) -> list:
    attack = []  # return list of ordered pairs
    a = 0
    b = 0  # ordered pair for checking

    # find location of pawn p, value 2 in array[x, y]
    n = np.where(x == 2)
    p = np.concatenate((n[0], n[1]))

    # check for knights
    if p[0] <= 2:  # checking for top half
        a = p[0]+2  # down 2
        if p[1] < 4:
            b = p[1]+1  # right 1
            if x[a, b] == 1:  # if knight
                attack.append((a, b))
        if p[1] > 0:
            b = p[1]-1  # left 1
            if x[a, b] == 1:  # if knight
                attack.append((a, b))
    if p[0] >= 2:  # checking for bottom half
        a = p[0]-2  # up 2
        if p[1] < 4:
            b = p[1]+1  # right 1
            if x[a, b] == 1:  # if knight
                attack.append((a, b))
        if p[1] > 0:
            b = p[1]-1  # left 1
            if x[a, b] == 1:  # if knight
                attack.append((a, b))
    if p[1] <= 2:  # checking for left half
        b = p[1]+2  # right 2
        if p[0] < 4:
            a = p[0]+1  # down 1
            if x[a, b] == 1:  # if knight
                attack.append((a, b))
        if p[0] > 0:
            a = p[0]-1  # up 1
            if x[a, b] == 1:  # if knight
                attack.append((a, b))
    if p[1] >= 2:  # checking for right half
        b = p[1]-2  # left 2
        if p[0] < 4:
            a = p[0]+1  # down 1
            if x[a, b] == 1:  # if knight
                attack.append((a, b))
        if p[0] > 0:
            a = p[0]-1  # up 1
            if x[a, b] == 1:  # if knight
                attack.append((a, b))

    return attack


def p5_a(x: dict) -> int:
    n = 0
    for a in x:
        if not x[a]:
            n += 1
    return n


def p5_b(x: dict) -> int:
    n = 0
    for a in x:
        if x[a]:
            n += 1
    return n


def p5_c(x: dict) -> list:
    # return unique edges as list of tuples
    y = x.copy()
    n = []
    for a in y:  # for each key
        if y[a]:  # if it has connected nodes
            for b in y[a]:  # for each element of key
                n.append((a, b))  # add pair
                for p in y[b]:
                    if p == a:
                        y[b].remove(p)
    return n


def p5_d(x: dict) -> np.array:
    len(x)
    k = []  # individual lists
    f = []  # list of lists
    for n in range(0, len(x)):  # create list of 0's
        k.append(0)
    for a in x:  # for each key:
        m = k.copy()  # copy list of 0's
        for b in x[a]:
            m[ord(b) - 65] = 1  # change to 1's
        f.append(m)
    npa = np.array(f)
    return npa


# Question 6
class PriorityQueue(object):
    # hard code a dictionary, ordered with price low to high
    def __init__(self):
        # dictionary hard code
        self.produce = {
            "carrot": 3.3,
            "banana": 4.5,
            "apple": 5.0,
            "orange": 5.0,
            "kiwi": 7.4,
            "mango": 9.1,
            "pineapple": 9.1
        }
        self.pq = []
        self.element = []

    def push(self, x):
        price = self.produce[x]
        if len(self.pq) == 0:
            self.pq.append((x, price))  # add product, price
        else:
            for i in range(0, len(self.pq)):
                if self.pq[i][1] >= price:  # if price of element in list <= price of inserting element
                    self.pq.insert(0, (x, price))  # insert element
                    break  # exit for loop
                elif i == len(self.pq)-1:  # if element is most expensive
                    self.pq.append((x, price))

    def pop(self):
        self.element = self.pq.pop()
        return self.element[0]

    def is_empty(self):
        if len(self.pq) == 0:
            return 1
        else:
            return 0


if __name__ == '__main__':
    print(p1(k=8))
    print('-----------------------------')
    print(p2_a(x=[], y=[1, 3, 5]))
    print(p2_b(x=[2, 4, 6], y=[]))
    print(p2_c(x=[1, 3, 5, 7], y=[1, 2, 5, 6]))
    print(p2_d(x=[1, 3, 5, 7], y=[1, 2, 5, 6]))
    print('------------------------------')
    print(p3_a(x={1, 3, 5, 7}, y={1, 2, 5, 6}, z={7, 8, 9, 1}))
    print(p3_b(x={1, 3, 5, 7}, y={1, 2, 5, 6}, z={7, 8, 9, 1}))
    print(p3_c(x={1, 3, 5, 7}, y={1, 2, 5, 6}, z={7, 8, 9, 1}))
    print('------------------------------')
    print(p4_a())
    print(p4_b(p4_a()))
    print('------------------------------')
    graph = {
        'A': ['D', 'E'],
        'B': ['E', 'F'],
        'C': ['E'],
        'D': ['A', 'E'],
        'E': ['A', 'B', 'C', 'D'],
        'F': ['B'],
        'G': []
    }
    print(p5_a(graph))
    print(p5_b(graph))
    print(p5_c(graph))
    print(p5_d(graph))
    print('------------------------------')
    pq = PriorityQueue()
    pq.push('apple')
    pq.push('kiwi')
    pq.push('orange')
    while not pq.is_empty():
        print(pq.pop())
