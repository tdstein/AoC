from sys import stdin

def parse(s):
    return int(s.split(' ')[1])

x, y = 0, 0
for line in stdin:
    if line.startswith('forward'):
        x += parse(line)
    if line.startswith('up'):
        y -= parse(line)
    if line.startswith('down'):
        y += parse(line)
print(x * y)