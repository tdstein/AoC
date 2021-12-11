
t = 0
p = {}
for x in open(0):
    if not x.strip():
        if len(p) == 8 or (len(p) == 7 and 'cid' not in p):
            t += 1
        p = {}
    else:
        for y in x.strip().split(' '):
            [k, v] = y.strip().split(':')
            p[k] = v
print(t)
