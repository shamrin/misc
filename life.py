from collections import Counter
import os
import time


def neighbor_cells(cell):
    x, y = cell
    yield x - 1, y - 1
    yield x - 1, y
    yield x - 1, y + 1
    yield x, y - 1
    yield x, y + 1
    yield x + 1, y - 1
    yield x + 1, y
    yield x + 1, y + 1


def advance(board):
    neighbors = Counter(neighbor for c in board for neighbor in neighbor_cells(c))
    return {c for c, n in neighbors.items() if n == 3 or (n == 2 and c in board)}


def draw(board):
    maxx = max(x for (x, y) in board)
    maxy = max(y for (x, y) in board)
    for y in range(0, maxy + 1):
        for x in range(0, maxx + 1):
            print("x" if (x, y) in board else " ", end="")
        print()


glider = """\
_x_
__x
xxx
"""

board = set()
for y, line in enumerate(glider.strip().split("\n")):
    for x, char in enumerate(line):
        if char == "x":
            board.add((x, y))

while True:
    os.system("clear")
    draw(board)
    time.sleep(0.1)
    board = advance(board)
