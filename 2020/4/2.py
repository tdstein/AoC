import re
t = 0
p = {}
for x in open(0):
    print(x)
    if not x.strip():
        if len(p) == 8 or (len(p) == 7 and 'cid' not in p):
            t += 1
        p = {}
    else:
        for y in x.strip().split(' '):
            [k, v] = y.strip().split(':')
            match k:
                case 'byr':
                    if not (len(v) == 4 and int(v) >= 1920 and int(v) <= 2002):
                        print(k, v)
                        break
                case 'iyr':
                    if not (len(v) == 4 and int(v) >= 2010 and int(v) <= 2020):
                        print(k, v)
                        break
                case 'eyr':
                    if not (len(v) == 4 and int(v) >= 2020 and int(v) <= 2030):
                        print(k, v)
                        break
                case 'hgt':
                    r = re.search(r"([0-9]+)(cm|in)", v)
                    if r is None:
                        print(k, v)
                        break
                    n = int(r.group(1))
                    m = r.group(2)
                    if m == 'in' and not (int(n) >= 59 and int(n) <= 76):
                        print(k, v)
                        break
                    if m == 'cm' and not (int(n) >= 150 and int(n) <= 193):
                        print(k, v)
                        break
                case 'hcl':
                    if not re.fullmatch(r"#[0-9a-f]{6}", v):
                        print(k, v)
                        break
                case 'ecl':
                    if not (v in { 'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth' }):
                        print(k, v)
                        break
                case 'pid':
                    if not re.fullmatch(r"[0-9]{9}", v):
                        print(k, v)
                        break
            p[k] = v
print(t)