from sys import stdin


def parse(s):
    return int(s.split(' ')[1])


x, y, aim = 0, 0, 0
for line in stdin:
    if line.startswith('forward'):
        x += parse(line)
        y += parse(line) * aim
    if line.startswith('up'):
        aim -= parse(line)
    if line.startswith('down'):
        aim += parse(line)
print(x * y)
