from functools import reduce

v = open(0).read().strip()
v = [ord(x) - 48 for x in list(v)]
v = [x if x < 10 else x + 58 - 65 for x in v]
v = [x & 0b1111 for x in v]
v = bytearray(map(lambda x, y: (x << 4) | y, v[::2], v[1::2]))


def s(v, n):
    j = int(n / 8)
    v = v[j:]
    n = n % 8
    for i, (x, y) in enumerate(zip(v, v[1:] + bytes([0]))):
        x <<= n
        x %= 2 ** 8
        x |= (y >> (8 - n))
        v[i] = x
    return v


def parse(v):
    n = (v[0] & 0xE0) >> 5
    v = s(v, 3)
    t = (v[0] & 0xE0) >> 5
    v = s(v, 3)
    match t:
        case 4:
            c = 0
            while ((v[0] & 0x80) >> 7):
                v = s(v, 5)
                c += 5
            v = s(v, 5)
            c += 5
            return(n, v, 6 + c)
        case _:
            i = (v[0] & 0x80) >> 7
            v = s(v, 1)
            if i:
                l = 0
                l |= v[0] << 3
                l |= v[1] >> 5
                v = s(v, 11)
                i = 0
                for _ in range(l):
                    (m, v, c) = parse(v)
                    n += m
                    i += c
                return (n, v, 6 + 1 + 11 + i)
            else:
                l = 0
                l |= v[0] << 7
                l |= v[1] >> 1
                v = s(v, 15)
                w = bytearray(v[:int(l / 8) + 1])
                w[-1] = w[-1] >> 8 - (l % 8)
                w[-1] = w[-1] << 8 - (l % 8)
                i = 0
                while i < l:
                    (m, w, c) = parse(w)
                    n += m
                    i += c
                v = s(v, l)
                return (n, v, 6 + 1 + 15 + i)


(n, _, _) = parse(v)
print(n)
