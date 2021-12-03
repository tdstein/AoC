from sys import stdin

cur, prev, inc, win = 0, 0, 0, [0, 0, 0]
for line in stdin:
    win[0] = win[1]
    win[1] = win[2]
    win[2] = int(line)
    if win[0] != 0:
        if cur == 0:
            cur = sum(win)
        else:
            prev = cur
            cur = sum(win)
            if cur > prev:
                inc += 1
print(inc)
