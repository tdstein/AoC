v = [ [ y for y in x.strip() ] for x in open(0)]

j = 0
t = 0
for i, x in enumerate(v):
    n = x[j]
    j += 3
    j %= len(x)
    if n == '#':
        t += 1
print(t)