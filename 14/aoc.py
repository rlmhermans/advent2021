from collections import defaultdict

with open('input') as f:
    lines = f.read().splitlines()

polymer = defaultdict(int)
pairs = list(zip(lines[0][:-1], lines[0][1:]))
for left, right in pairs:
    polymer[left + right] += 1

rules = {}
for rule in lines[2:]:
    k, v = rule.split(' -> ')
    rules[k] = v

for _ in range(40):
    temp_polymer = defaultdict(int)
    for p in polymer:
        middle = rules[p]
        temp_polymer[p[0] + middle] += polymer[p]
        temp_polymer[middle + p[1]] += polymer[p]
    polymer = temp_polymer

hist = defaultdict(int)
for p in polymer:
    hist[p[0]] += polymer[p]
hist[p[1]] += 1

print(max(hist.values()) - min(hist.values()))