import numpy as np
import itertools as it

m = np.genfromtxt('input', dtype='int', delimiter=1)
windows = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
flashed = []

def cell_exists(y, x):
    return 0 <= x < len(m[0]) and 0 <= y < len(m)

def flash(y, x):
    if (y, x) not in flashed:
        flashed.append((y, x))
        
        for offset_y, offset_x in windows:
            neighbour_y, neighbour_x = (y + offset_y, x + offset_x)
            if cell_exists(neighbour_y, neighbour_x):
                m[neighbour_y, neighbour_x] += 1
                if m[neighbour_y, neighbour_x] > 9:
                    flash(neighbour_y, neighbour_x)

total_flashes = 0
i = 0
flashbang = False

while not flashbang:
    i += 1
    m = m + 1

    for y, x in it.product(range(0, len(m)), range(0, len(m[0]))):
        if m[y][x] > 9:
            flash(y, x)            

    for y, x in flashed:
        m[y][x] = 0
    
    total_flashes += len(flashed)

    if i == 100:
        print('Part 1:', total_flashes)

    if len(flashed) == 100:
        flashbang = True

    flashed.clear()

print('Part 2:', i)