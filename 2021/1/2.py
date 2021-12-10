from sys import stdin

inc = 0
win = [int(stdin.readline()), int(stdin.readline()), int(stdin.readline())]
cur = sum(win)
for line in stdin:
    win = win[1:] + [int(line)]
    prev = cur
    cur = sum(win)
    if cur > prev:
        inc += 1

print(inc)
