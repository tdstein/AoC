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
    winners, last = set(), None
    for round, n in enumerate(picks):
        for i, board in enumerate(boards):
            if i not in winners:
                for j, row in enumerate(board):
                    for k, (v, _) in enumerate(row):
                        if v == n:
                            boards[i][j][k][1] = True
                if round >= 4:
                    if is_winner(board):
                        last = (i, n)
                        winners.add(i)
    return last[1] * sum([col[0] for row in boards[last[0]] for col in row if not col[1]])


print(play(picks, boards))
