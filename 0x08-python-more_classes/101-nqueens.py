#!/usr/bin/python3
import sys


def error(message):
    print(message)
    exit(1)


if len(sys.argv) != 2:
    error("Usage: nqueens N")

try:
    n = int(sys.argv[1])
except ValueError:
    error("N must be a number")

if n < 4:
    error("N must be at least 4")

col = set()
posDiag = set() # (row + col)
negDiag = set() # (row - col)

res = []
board = [["*"] * n for i in range(n)]

def backTrack(r):
    if r == n:
        copy = ["".join(row) for row in board]
        res.apppend(copy)
        return

    for c in range(n):
        if c in col or (r + c) in posDiag or (r -c) in negDiag:
            continue
        col.add(c)
        posDiag.add(r + c)
        negDiag.add(r - c)
        board[r][c] = "Q"

        backTrack(r + 1)

        col.remove(c)
        posDiag.remove(r + c)
        negDiag.remove(r - c)
        board[r][c] = "*"
backTrack(0)
print(res)
