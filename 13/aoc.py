with open('input') as f:
    dots, instructions = f.read().split('\n\n')

coords = set()
for line in dots.split('\n'):
    x, y = line.split(',')
    coords.add((int(x),int(y)))

def fold(edge, coords, side):
    new_coords = set()
    for c in coords:
        if c[side] > edge:
            value = edge - (c[side] - edge)
            c = (value, c[1]) if side == 0 else (c[0], value)
        new_coords.add(c)

    return new_coords

for i in instructions.split('\n'):
    side = 1 if i[11] == 'y' else 0
    coords = fold(int(i[13:]), coords, side)

for y in range(6):
    for x in range(40):
        value = '#' if (x, y) in coords else '.'
        print(value, end='')

    print()