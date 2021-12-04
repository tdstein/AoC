from sys import stdin

inc = 0
cur = int(stdin.readline())
for line in stdin:
    prev = cur
    cur = int(line)
    if cur > prev:
        inc += 1

print(inc)
