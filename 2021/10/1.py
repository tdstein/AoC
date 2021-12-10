from collections import deque

k = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

p = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

t = 0
for x in open(0):
    s = deque()
    for y in x.strip():
        if y in k:
            s.append(y)
        else:
            if k[s.pop()] != y:
                t += p[y]

print(t)