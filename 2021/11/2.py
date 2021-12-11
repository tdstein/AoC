n = [[int(y) for y in x.strip()] for x in open(0)]

N = 10
M = 10


def flash(n, i, j):
    t = 0
    v = n[i][j]
    if v > 9:
        t += 1
        n[i][j] = 0
        for p in range(max(i-1, 0), min(i+2, M)):
            for q in range(max(j-1, 0), min(j+2, N)):
                if not (p == i and q == j) and n[p][q] != 0:
                    n[p][q] += 1
                    (n, tt) = flash(n, p, q)
                    t += tt
    return (n, t)


t = 0
while True:
    n = [[y+1 for y in x] for x in n]
    for i, x in enumerate(n):
        for j, y in enumerate(x):
            (n, tt) = flash(n, i, j)
    t += 1
    if sum([y for x in n for y in x]) == 0:
        break
print(t)
