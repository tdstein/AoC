def f(s, n):
    s = ''.join(format(x, '04b') for x in s)        
    s = s[n:]    
    return [int("".join(s[i:i+4]), 2) for i in range(0, len(s), 4)]



r = 0
v = open(0).read().strip()
v = [x for x in list(v)]
v = [ord(x) - 48 for x in list(v)]
v = [x if x < 10 else x + 58 - 65 for x in v]
v = [x & 0b1111 for x in v]

while sum(v) != 0:        
    h = (v[0] & 0b1110) >> 1        
    r += h
    t = ((v[0] & 0b0001) << 2) | ((v[1] & 0b1100) >> 2)        
    match t:
        case 4:
            v = f(v, 6)
            n = 0
            i = 0                
            while (v[0] & 0b1000) >> 3:
                v = f(v, 1)
                n |= v[0]
                n <<= 4                    
                v = f(v, 4)
                i += 1                    
            v = f(v, 1)
            s = int((i * 5) / 4) % 4
            a = v[0]
            a <<= s
            a >>= s
            n |= a                
            v = f(v, 4)
        case _:
            i = (v[1] & 0b0010) > 1                
            if i:                    
                l = (v[1] & 0b0001) << 10
                l |= v[2] << 6
                l |= v[3] << 2
                l |= (v[4] & 0b1100) >> 2                    
                v = f(v, 3 + 3 + 1 + 11)
            else:                    
                l = (v[1] & 0b0001) << 14
                l |= v[2] << 10
                l |= v[3] << 6
                l |= v[4] << 2
                l |= (v[5] & 0b1100) >> 2                    
                v = f(v, 3 + 3 + 1 + 15)
print(r)