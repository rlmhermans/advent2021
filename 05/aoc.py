with open('input') as f:
    input = [int(x) for x in f.read().split(',')]

days = 256
lifetime = 9
fish = [input.count(day) for day in range(lifetime)]

for day in range(days):
    temp_fish = fish.pop(0)
    fish.append(temp_fish)
    fish[6] += temp_fish

print(sum(fish))