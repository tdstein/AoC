from sys import stdin

from collections import Counter

fish = [int(v) for line in stdin for v in line.strip().split(',') ]
fish = Counter(fish)

for i in range(256):
    spawn = fish[0]
    for i in range(8):
        fish[i] = fish[i+1]
    fish[8] = spawn
    fish[6] += spawn

print(sum(fish.values()))