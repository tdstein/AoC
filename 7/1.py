from sys import stdin

c = [int(v) for v in stdin.readline().strip().split(',')]
m = sorted(c)[len(c)/2]
v = sum([abs(v - m) for v in c])
print(v)
