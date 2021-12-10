v = [ int(x.strip()) for x in open(0)]
for x in v:
    for y in v:
        if x + y == 2020:
            print(x * y)
            exit()
