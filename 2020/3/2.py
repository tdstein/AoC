v = [[y for y in x.strip()] for x in open(0)]

s = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

c = 1
for (q, p) in s:
    t = 0
    j = 0
    for i in range(0, len(v), p):
        n = v[i][j]
        j += q
        j %= len(v[i])
        if n == '#':
            t += 1
    c *= t
print(c)
