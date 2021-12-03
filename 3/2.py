with open('in', 'r') as f:
    lines = [ line.strip() for line in f ]

cc = len(lines[0])
lines = [ int(line, 2) for line in lines ]

ogr = lines
ocr = lines

for idx in range(0, cc):
    if len(ogr) == 1:
        break
    m = pow(2, (cc - idx - 1))
    vs = [ v & m for v in ogr]
    pos = sum([1 for v in vs if v > 0])
    if pos > int((len(vs) - 1) / 2):
        ogr = [ ogr[idx] for idx, v in enumerate(vs) if v > 0] 
    else:
        ogr = [ ogr[idx] for idx, v in enumerate(vs) if v == 0]

for idx in range(0, cc):
    if len(ocr) == 1:
        break
    m = pow(2, (cc - idx - 1))
    vs = [ v & m for v in ocr]
    pos = sum([1 for v in vs if v > 0])
    if pos > int((len(vs) - 1) / 2):
        ocr = [ ocr[idx] for idx, v in enumerate(vs) if v == 0] 
    else:
        ocr = [ ocr[idx] for idx, v in enumerate(vs) if v > 0]

print(ogr[0] * ocr[0])