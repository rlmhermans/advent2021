import numpy as np

matrix = np.genfromtxt('input', dtype='int', delimiter=1)

low_points = []
basin_starts = []

for current_x, current_y in [(x,y) for x in range(len(matrix[0])) for y in range(len(matrix))]:
    values = []

    current_value = matrix[current_y][current_x]
    values.append(current_value)

    if current_y > 0:
        values.append(matrix[current_y - 1][current_x])

    if current_y < len(matrix) - 1:
        values.append(matrix[current_y + 1][current_x])

    if current_x > 0:
        values.append(matrix[current_y][current_x - 1])

    if current_x < len(matrix[0]) - 1:
        values.append(matrix[current_y][current_x + 1])

    if min(values) == current_value and values.count(current_value) is not len(values):
        low_points.append(current_value)
        basin_starts.append((current_x, current_y))

print(sum(low_points) + len(low_points))

def neighbours(x, y):
    neighbours = []

    if y > 0:
        neighbours.append((x, y - 1))

    if y < len(matrix) - 1:
        neighbours.append((x, y + 1))

    if x > 0:
        neighbours.append((x - 1, y))

    if x < len(matrix[0]) - 1:
        neighbours.append((x + 1, y))

    return neighbours

def spread(current, basin):
    basin.append(current)
    (x, y) = current

    size = 0

    for n in neighbours(x, y):
        (n_x, n_y) = n

        if matrix[n_y][n_x] != 9 and n not in basin:
            size += spread(n, basin)

    return 1 + size

basin_sizes = []

for basin_start in basin_starts:
    basin_sizes.append(spread(basin_start, []))

basin_sizes.sort(reverse=True)
print(basin_sizes[0]*basin_sizes[1]*basin_sizes[2])