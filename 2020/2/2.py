t = 0
for x in open(0):
    x = x.strip().split(' ')
    [i, j] = [int(y) - 1 for y in x[0].split('-')]
    v = x[1][0]
    p = x[2]
    a = p[i] == v
    b = p[j] == v 
    if (a and not b) or (not a and b):
        t += 1
print(t)