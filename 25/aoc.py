with open('input') as f:
    input = f.read().splitlines()

south_bound_herd = set()
east_bound_herd = set()

width = len(input[0])
height = len(input)

y = 0
for line in input:
    x = 0
    for c in line:
        if c == 'v': south_bound_herd.add((y, x))
        elif c == '>': east_bound_herd.add((y, x))
        x += 1
    y += 1

moved = True
state = 0
while moved:
    state += 1
    moved = False

    new_east_bound_herd = set()
    both_herds = east_bound_herd | south_bound_herd
    for y, x in east_bound_herd:
        next_x = x + 1
        if next_x == width: next_x = 0
        if (y, next_x) not in both_herds:
            new_east_bound_herd.add((y, next_x))
            moved = True
        else:
            new_east_bound_herd.add((y, x))
    
    east_bound_herd = new_east_bound_herd

    new_south_bound_herd = set()
    both_herds = east_bound_herd | south_bound_herd
    for y, x in south_bound_herd:
        next_y = y + 1
        if next_y == height: next_y = 0
        if (next_y, x) not in both_herds:
            new_south_bound_herd.add((next_y, x))
            moved = True
        else:
            new_south_bound_herd.add((y, x))

    south_bound_herd = new_south_bound_herd

print('Part 1:', state)