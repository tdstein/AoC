import re

from sys import stdin

picks = [int(v) for v in stdin.readline().strip().split(',')]
lines = [re.split('\s+', line.strip()) for line in stdin if line.strip()]
lines = [[[int(v), False] for v in line] for line in lines]
boards = [lines[n:n+5] for n in range(0, len(lines), 5)]


def is_winner(board):
    for i in range(5):
        if len([s for [_, s] in board[i] if s]) == 5:
            return True
        if len([row[i][1] for row in board if row[i][1]]) == 5:
            return True


def play(picks, boards):
    for round, n in enumerate(picks):
        for i, board in enumerate(boards):
            for j, row in enumerate(board):
                for k, (v, _) in enumerate(row):
                    if v == n:
                        boards[i][j][k][1] = True
            if round >= 4:
                if is_winner(board):
                    return n * sum([col[0] for row in board for col in row if not col[1]])


print(play(picks, boards))
