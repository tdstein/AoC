from sys import stdin

lines = [line.strip().split(' -> ') for line in stdin]
lines = [[points.split(',') for points in line] for line in lines]
lines = [[[int(v) for v in point] for point in line] for line in lines]

mx = max([x for line in lines for [x, _] in line]) + 1
my = max([y for line in lines for [_, y] in line]) + 1

m = [[0 for i in range(mx)] for j in range(my)]

for [[x1, y1], [x2, y2]] in lines:
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            m[y][x1] += 1
    if y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            m[y1][x] += 1
    if abs(x2 - x1) == abs(y2 - y1):
        mn = [x1, y1] if y1 < y2 else [x2, y2]
        mx = [x2, y2] if y1 < y2 else [x1, y1]
        dir = 1 if mn[0] < mx[0] else -1
        if mn[0] < mx[0]:
            for i, x in enumerate(range(mn[0], mx[0] + 1)):
                m[mn[1] + i][x] += 1
        else:
            for i, x in enumerate(range(mn[0], mx[0] - 1, -1)):
                m[mn[1] + i][x] += 1


print(sum([1 for row in m for v in row if v > 1]))
