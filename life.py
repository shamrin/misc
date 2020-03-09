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
    maxx, maxy = 80, 24
    for y in range(maxy):
        print("".join("x" if (x, y) in board else " " for x in range(maxx)))


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
