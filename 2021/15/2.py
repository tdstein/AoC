import networkx as nx

v = [[int(y) for y in x.strip()] for x in open(0)]

M = len(v)
T = 5

w = [[0] * (M * T) for _ in range(M * T)]
for i in range(M * T):
    for j in range(M * T):
        n = v[i % M][j % M]
        x = int(i / M)
        y = int(j / M)
        m = (n + x + y)
        r = m % 10
        w[i][j] = r + (1 * int(m / 10))


def s(i, j):
    return str(i) + ',' + str(j)


def d(s):
    return [int(_) for _ in s.split(',')]


G = nx.DiGraph()
for i in range(M * T):
    for j in range(M * T):
        a = [[y, j] for y in range(max(i-1, 0), min(i+2, M * T)) if y != i]
        b = [[i, y] for y in range(max(j-1, 0), min(j+2, M * T)) if y != j]
        for [p, q] in a + b:
            G.add_edge(s(i, j), s(p, q), weight=w[p][q])

p = nx.astar_path(G, s(0, 0), s(M * T - 1, M * T - 1), weight='weight')
p = [d(_) for _ in p[1:]]
print(sum([w[i][j] for [i, j] in p]))
