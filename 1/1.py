from sys import stdin

cur, prev, inc = 0, 0, 0
for line in stdin:
    if cur == 0:
        cur = int(line)
    else:
        prev = cur
        cur = int(line)
        if cur > prev:
            inc += 1
print(inc)
