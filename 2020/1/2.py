v = [ int(x.strip()) for x in open(0)]
for x in v:
    for y in v:
        for z in v:
            if x + y + z == 2020:
                print(x * y * z)
                exit()
