s = 0
for x, y in [x.split('|') for x in open(0)]:
    l = {len(s): set(s) for s in x.split()}

    n = ''
    for o in map(set, y.split()):
        match len(o), len(o & l[4]), len(o & l[2]):
            case 2, _, _: n += '1'
            case 3, _, _: n += '7'
            case 4, _, _: n += '4'
            case 7, _, _: n += '8'
            case 5, 2, _: n += '2'
            case 5, 3, 1: n += '5'
            case 5, 3, 2: n += '3'
            case 6, 4, _: n += '9'
            case 6, 3, 1: n += '6'
            case 6, 3, 2: n += '0'
    s += int(n)

print(s)
