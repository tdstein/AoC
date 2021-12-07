from sys import stdin
from math import floor, ceil


def t(v):
    return v*(v+1)/2


c = [int(v) for v in stdin.readline().strip().split(',')]
m = float(sum(c)) / len(c)
v = min([sum([t(abs(v - i)) for v in c]) for i in [int(floor(m)), int(ceil(m))]])
print(v)
