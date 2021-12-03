with open('in', 'r') as f:
    lines = [ line.strip() for line in f ]

cc = len(lines[0])
lines = [ int(line, 2) for line in lines ]

gr, er = 0, 0
for idx in range(0, cc):
    m = pow(2, (cc - idx - 1))
    vs = sorted([ v & m for v in lines ])
    if vs[int((len(vs) - 1) / 2)] > 0:
        gr = gr | m
    else:
        er = er | m

print(gr * er)