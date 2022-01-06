with open('input') as f:
    input = f.read().splitlines()

cubes = []

def length(x, y):
    return abs(x - y) + 1

def blocks_in_cube(cube):
    x_min, x_max, y_min, y_max, z_min, z_max = cube
    return length(x_min, x_max) * length(y_min, y_max) * length(z_min, z_max)

def intersects(this, that):
    this_x_min, this_x_max, this_y_min, this_y_max, this_z_min, this_z_max = this
    that_x_min, that_x_max, that_y_min, that_y_max, that_z_min, that_z_max = that

    x_overlaps = that_x_min <= this_x_min <= that_x_max or this_x_min <= that_x_min <= this_x_max
    y_overlaps = that_y_min <= this_y_min <= that_y_max or this_y_min <= that_y_min <= this_y_max
    z_overlaps = that_z_min <= this_z_min <= that_z_max or this_z_min <= that_z_min <= this_z_max

    return x_overlaps and y_overlaps and z_overlaps

def split(this, that):
    new_cubes = []
    this_x_min, this_x_max, this_y_min, this_y_max, this_z_min, this_z_max = this
    that_x_min, that_x_max, that_y_min, that_y_max, that_z_min, that_z_max = that

    left_width, right_width, top_width, bottom_width = [0,0,0,0]
    # left
    if this_x_min < that_x_min and this_x_max >= that_x_min:
        new_cubes.append([this_x_min, that_x_min-1, this_y_min, this_y_max, this_z_min, this_z_max])
        left_width = length(this_x_min, that_x_min-1)
    # right
    if this_x_max > that_x_max and this_x_min <= that_x_max:
        new_cubes.append([that_x_max + 1, this_x_max, this_y_min, this_y_max, this_z_min, this_z_max])
        right_width = length(that_x_max + 1, this_x_max)
    # top
    if this_y_min < that_y_min and this_y_max >= that_y_min:
        new_cubes.append([this_x_min + left_width, this_x_max - right_width, this_y_min, that_y_min-1, this_z_min, this_z_max])
        top_width = length(this_y_min, that_y_min-1)
    # bottom  
    if this_y_max > that_y_max and this_y_min <= that_y_max:
        new_cubes.append([this_x_min + left_width, this_x_max - right_width, that_y_max + 1, this_y_max, this_z_min, this_z_max])
        bottom_width = length(that_y_max + 1, this_y_max)
    # front
    if this_z_min < that_z_min and this_z_max >= that_z_min:
        new_cubes.append([this_x_min + left_width, this_x_max - right_width, this_y_min + top_width, this_y_max - bottom_width, this_z_min, that_z_min-1])
    # back
    if this_z_max > that_z_max and this_z_min <= that_z_max:
        new_cubes.append([this_x_min + left_width, this_x_max - right_width, this_y_min + top_width, this_y_max - bottom_width, that_z_max + 1, this_z_max])

    return new_cubes

for line in input:
    command, coors = line.split(' ')
    x_min, x_max = map(int, line[line.index('x')+2: line.index(',y')].split('..'))
    y_min, y_max = map(int, line[line.index('y')+2: line.index(',z')].split('..'))
    z_min, z_max = map(int, line[line.index('z')+2:].split('..'))

    cube = [x_min, x_max, y_min, y_max, z_min, z_max]
    
    # if x_min >= -50 and x_max <= 50 and y_min >= -50 and y_max <= 50 and z_min >= -50 and z_max <= 50: # Part 1
    new_cubes = []

    for c in cubes:
        if intersects(c, cube):
            new_cubes.extend(split(c, cube))
        else:
            new_cubes.append(c)

    if command in 'on': new_cubes.append(cube)

    cubes = new_cubes

total = 0
for cube in cubes:
    total += blocks_in_cube(cube)

print('Answer:', total)