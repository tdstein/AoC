from math import floor, ceil


def t(x): return x * (x + 1) / 2


for x in open(0):
    n = [int(y) for y in x.split(',')]
    m = float(sum(n)) / len(n)
    v = min([sum([t(abs(v - i)) for v in n]) for i in [floor(m), ceil(m)]])
    print(int(v))
