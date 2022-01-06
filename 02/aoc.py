with open('test') as f:
    input = f.read().splitlines()

course = {
    'forward': 0,
    'up': 0,
    'down': 0
}

for line in input:
    course[line.split(' ')[0]] += int(line.split(' ')[1])

print('Part 1:', course['forward'] * (course['down'] - course['up']))

horizontal = 0
depth = 0
aim = 0

for line in input:
    command = line.split(' ')[0]
    value = int(line.split(' ')[1])

    if command in 'forward': 
        horizontal += value
        depth += aim * value
    elif command in 'down':
        aim += value
    else:
        aim -= value

print('Part 2:', horizontal * depth)