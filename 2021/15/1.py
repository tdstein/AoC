import networkx as nx

v = [[int(y) for y in x.strip()] for x in open(0)]


M = len(v)
N = len(v[0])


def s(i, j):
    return str(i) + ',' + str(j)


def d(s):
    return [int(_) for _ in s.split(',')]


G = nx.DiGraph()
for i in range(M):
    for j in range(N):
        a = [[y, j] for y in range(max(i-1, 0), min(i+2, M)) if y != i]
        b = [[i, y] for y in range(max(j-1, 0), min(j+2, N)) if y != j]
        for [p, q] in a + b:
            G.add_edge(s(i, j), s(p, q), weight=v[p][q])

p = nx.astar_path(G, s(0, 0), s(M - 1, N - 1), weight='weight')
p = [d(_) for _ in p[1:]]
print(sum([v[i][j] for [i, j] in p]))
