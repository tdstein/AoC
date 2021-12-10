m = [[int(y) for y in list(x.strip())] for x in open(0)]

c = 0
for i, x in enumerate(m):
    for j, y in enumerate(x):
        n = []
        if i > 0:
            n.append(m[i-1][j])
        if i+1 < len(m):
            n.append(m[i+1][j])
        if j > 0:
            n.append(m[i][j-1])
        if j+1 < len(x):
            n.append(m[i][j+1])
        if y < min(n):
            c += y+1

print(c)
