import numpy

with open('input') as f:
    input = [int(x) for x in f.read().split(',')]

median = numpy.median(input)
fuel = 0

for x in input:
    fuel += abs(median - x)

print('Part 1: ', fuel)

# least_fuel = 9999999999999
# for i in range(2000):
#     fuel = 0

#     for x in input:
#         distance = abs(i - x)
#         fuel += distance * (distance + 1) / 2

#     print(fuel)
#     if fuel < least_fuel:
#         least_fuel = fuel

# print('Part 2: ', least_fuel)

mean = round(numpy.mean(input))
fuel = 0

for x in input:
    distance = abs(mean - x)
    fuel += distance * (distance + 1) / 2

print('Part 2: ', fuel)