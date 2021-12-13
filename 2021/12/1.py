from collections import defaultdict

n = defaultdict(list, {})
for x in open(0):
    a, b = x.strip().split('-')
    n[a].append(b)
    n[b].append(a)

n = {**n}


def t(n, k, h=[]):
    if k == 'end':
        return 1
    c = 0
    for x in n[k]:
        if x not in h or x == x.upper():
            c += t(n, x, (h + [k]))
    return c


print(t(n, 'start'))
