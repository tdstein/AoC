n = [x.strip() for x in open(0)]
i = n.index('')
p = n[:i]
f = n[i+1:]
p = [[int(y) for y in x.split(',')] for x in p]
f = [x[11:].split('=') for x in f]
f = [[a, int(c)] for [a, c] in f]

M = max([x for [x, _] in p])
N = max([y for [_, y] in p])
for i in f:
    a, c = i
    for j, [x, y] in enumerate(p):
        match a:
            case 'x':
                M = min(M, c)
                if x > c:
                    p[j] = [c - (x - c), y]
            case 'y':
                N = min(N, c)
                if y > c:
                    p[j] = [x, c - (y - c)]

m = [[' ' for _ in range(M)] for _ in range(N)]
for [x, y] in p:
    m[y][x] = '#'

[print(_) for _ in m]
