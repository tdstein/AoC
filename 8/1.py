s = 0
for _, x in [x.split('|') for x in open(0)]:
    s += len([y for y in x.split() if len(y) in set([2, 3, 4, 7])])

print(s)
