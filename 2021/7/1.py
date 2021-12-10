for x in open(0):
    n = sorted([int(y) for y in x.split(',')])
    m = n[int(len(n)/2)]
    v = sum([abs(v - m) for v in n])
    print(v)