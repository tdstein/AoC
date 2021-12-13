n = [x.strip() for x in open(0)]
i = n.index('')
p = n[:i]
f = n[i+1:]
p = [[int(y) for y in x.split(',')] for x in p]
f = [x[11:].split('=') for x in f[:1]]
f = [[a, int(c)] for [a, c] in f]


a, c = f[0]
for j, [x, y] in enumerate(p):
    match a:
        case 'x':
            if x > c:
                p[j] = [c - (x - c), y]
        case 'y':
            if y > c:
                p[j] = [x, c - (y - c)]

print(len(set([",".join([str(y) for y in x]) for x in p])))
