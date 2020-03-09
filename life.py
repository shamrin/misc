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


glider = """
_x_
__x
xxx
"""

glider = glider.strip().split("\n")

b = set((x, y) for y, line in enumerate(glider) for x, c in enumerate(line) if c == "x")
while True:
    os.system("clear")
    draw(b)
    time.sleep(0.1)
    b = advance(b)
