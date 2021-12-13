from collections import defaultdict

n = defaultdict(list, {})
for x in open(0):
    a, b = x.strip().split('-')
    if b != 'start':
        n[a].append(b)
    if a != 'start':
        n[b].append(a)

n = {**n}


def t(n, k, h=[]):
    if k == 'end':
        return 1
    c = 0
    m = h + [k]
    m = max([m.count(x) for x in m if x == x.lower()])
    for x in n[k]:
        if m < 2 or x not in h or x == x.upper():
            c += t(n, x, (h + [k]))
    return c


print(t(n, 'start'))
