from sys import stdin

vs = []
for line in stdin:
    line = line.strip()
    cc = len(line)
    vs.append(int(line, 2))


def x(vs, f):
    for idx in range(0, cc):
        mask = pow(2, (cc - idx - 1))
        ms = [v & mask for v in vs]
        s = sum([1 for v in ms if v > 0])
        mid = int((len(ms) - 1) / 2)
        if s > mid:
            vs = [vs[idx] for idx, v in enumerate(ms) if f(v)]
        else:
            vs = [vs[idx] for idx, v in enumerate(ms) if not f(v)]
        if len(vs) == 1:
            return vs[0]


ogr = x(vs, lambda x: x > 0)
ocr = x(vs, lambda x: x == 0)

print(ogr * ocr)
