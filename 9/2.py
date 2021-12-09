import networkx as nx

from functools import reduce

m = [[int(y) for y in list(x.strip())] for x in open(0)]
m = [[1 if y != 9 else 0 for y in x] for x in m]

G = nx.Graph()
for i, x in enumerate(m):
    def p(i, j): return len(x) * i + j
    for j, y in enumerate(x):
        if y == 1:
            s = p(i, j)
            if i > 0:
                if m[i-1][j] == 1:
                    G.add_edge(s, p(i-1, j))
            if i + 1 < len(m):
                if m[i+1][j] == 1:
                    G.add_edge(s, p(i+1, j))
            if j > 0:
                if m[i][j-1] == 1:
                    G.add_edge(s, p(i, j-1))
            if j + 1 < len(x):
                if m[i][j+1] == 1:
                    G.add_edge(s, p(i, j+1))


S = sorted([len(g) for g in nx.connected_components(G)], reverse=True)

print(reduce(lambda x, y: x * y, S[:3]))
