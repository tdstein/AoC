from sys import stdin

lines = []
for line in stdin:
    line = line.strip().split(' -> ')
    line = [point.split(',') for point in line]
    line = [[int(v) for v in point] for point in line]
    line = sorted(line)
    lines.append(line)

lines = sorted(lines)

mx = max([x for line in lines for [x, _] in line]) + 1
my = max([y for line in lines for [_, y] in line]) + 1

m = [[0 for i in range(mx)] for j in range(my)]

for [[x1, y1], [x2, y2]] in lines:
    if y1 == y2:
        for i in range(x1, x2+1):
            m[y1][i] += 1
    if x1 == x2:
        for i in range(min(y1, y2), max(y1, y2)+1):
            m[i][x1] += 1
    
print(sum([1 for line in m for v in line if v > 1]))