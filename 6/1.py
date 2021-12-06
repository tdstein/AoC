from sys import stdin

fish = [ int(v) for line in stdin for v in line.strip().split(',') ]

for i in range(80):
    spawn = []
    for i, v in enumerate(fish):
        if v == 0:
            spawn.append(8)
            fish[i] = 6
        else:
            fish[i] -= 1
    fish.extend(spawn)

print(len(fish))