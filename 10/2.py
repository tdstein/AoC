from collections import deque

k = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

t = []
for x in open(0):
    s = deque()
    for y in x.strip():
        if y in k:
            s.append(y)
        else:
            if k[s.pop()] != y:
                s.clear()
                break
    if s:
        v = 0
        for z in reversed(s):
            v *= 5
            v += list(k).index(z) + 1
        t += [v]

print(sorted(t)[int(len(t)/2)])
