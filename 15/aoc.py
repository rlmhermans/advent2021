import numpy as np
from collections import defaultdict
import heapq

m = np.genfromtxt('input', dtype='int', delimiter=1)
n = np.copy(m)
for _ in range(4):
    n += 1
    m = np.concatenate((m, n), 0)

n = np.copy(m)
for _ in range(4):
    n += 1
    m = np.concatenate((m, n), 1)

width, height = np.shape(m)

for y in range(height):
    for x in range(width):
        if m[y][x] > 9:
            m[y][x] -= 9

last = (height-1, width-1)

def get_next(y, x):
    next_cells = []

    if y > 0:
        next_cells.append((y-1, x))

    if y < last[0]:
        next_cells.append((y+1, x))

    if x > 0:
        next_cells.append((y, x-1))

    if x < last[1]:
        next_cells.append((y, x+1))

    return next_cells

unvisited_risks = [(0, (0,0))]
visited = set()

while len(unvisited_risks) > 0:
    current_risk, current = heapq.heappop(unvisited_risks)

    if current in visited: continue

    if current == last: break
    visited.add(current)
    neighbours = get_next(current[0], current[1])

    for n in neighbours: 
        if n not in visited:
            heapq.heappush(unvisited_risks, (current_risk + m[n[0]][n[1]], n))

print('Part 2:', current_risk)