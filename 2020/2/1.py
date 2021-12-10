t = 0
for x in open(0):
    x = x.strip().split(' ')
    [min, max] = [int(y) for y in x[0].split('-')]
    v = x[1][0]
    p = x[2]
    c = sum([1 for y in p if y == v])
    if c >= min and c <= max:
        t += 1
print(t)