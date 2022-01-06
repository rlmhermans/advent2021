with open('input') as f:
    input = f.read().splitlines()

# part 1
depth = int(input[0])
times_increased = 0

for line in input:
    new_depth = int(line)
    if new_depth > depth:
        times_increased += 1

    depth = new_depth

print('Part 1:', times_increased)

# part 2
depth = int(input[0]) + int(input[1]) + int(input[2])
times_increased = 0

for i in range(3, len(input)):
    new_depth = int(input[i-2]) + int(input[i-1]) + int(input[i])
    if new_depth > depth:
        times_increased += 1

    depth = new_depth

print('Part 2:', times_increased)