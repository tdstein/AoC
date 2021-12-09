from sys import stdin

s = set([2, 4, 3, 7])
o = [[v for v in line.split('|')[1].strip().split(' ')] for line in stdin]
r = sum([sum([1 for v in line if len(v) in s]) for line in o])
print(r)
