with open('input') as f:
    input = f.read().splitlines()

width = 990
vent_lines = [[0] * width for i in range(width)]

for line in input:
    coords = line.split(' -> ')
    start = (int(coords[0].split(',')[0]), int(coords[0].split(',')[1]))
    end = (int(coords[1].split(',')[0]), int(coords[1].split(',')[1]))

    if start[0] == end[0]:
        if start[1] < end[1]:
            for i in range(start[1], end[1] + 1):
                vent_lines[i][start[0]] += 1
        if start[1] >= end[1]:
            for i in range(start[1], end[1] - 1, -1):
                vent_lines[i][start[0]] += 1
    elif start[1] == end[1]:
        if start[0] < end[0]:
            for i in range(start[0], end[0] + 1):
                vent_lines[start[1]][i] += 1
        if start[0] >= end[0]:
            for i in range(start[0], end[0] - 1, -1):
                vent_lines[start[1]][i] += 1
    else:
        if start[0] < end[0] and start[1] < end[1]:
            i = start[0]
            for j in range(start[1], end[1] + 1):
                vent_lines[j][i] += 1
                i += 1
        if start[0] >= end[0] and start[1] >= end[1]:
            i = start[0]
            for j in range(start[1], end[1] - 1, -1):
                vent_lines[j][i] += 1
                i -= 1
        if start[0] < end[0] and start[1] >= end[1]:
            i = start[0]
            for j in range(start[1], end[1] - 1, -1):
                vent_lines[j][i] += 1
                i += 1
        if start[0] >= end[0] and start[1] < end[1]:
            i = start[0]
            for j in range(start[1], end[1] + 1):
                vent_lines[j][i] += 1
                i -= 1

count = 0

for line in vent_lines:
    for cell in line:
        if cell > 1:
            count += 1

print(count)