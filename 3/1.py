from sys import stdin

vs = []
for line in stdin:
    line = line.strip()
    cc = len(line)
    vs.append(int(line, 2))


gr, er = 0, 0
for idx in range(0, cc):
    mask = pow(2, (cc - idx - 1))
    ms = sorted([v & mask for v in vs])
    if ms[int((len(ms) - 1) / 2)] > 0:
        gr = gr | mask
    else:
        er = er | mask

print(gr * er)
