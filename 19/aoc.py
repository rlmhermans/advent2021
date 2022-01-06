from collections import Counter

with open('input') as f:
    input = f.read().splitlines()

def distance(point_a, point_b):
    x_a, y_a, z_a = point_a
    x_b, y_b, z_b = point_b
    return abs(x_a - x_b) + abs(y_a - y_b) + abs(z_a - z_b)

def vector(point_a, point_b):
    x_a, y_a, z_a = point_a
    x_b, y_b, z_b = point_b
    return (x_b - x_a, y_b - y_a, z_b - z_a)

def get_vectors(scan):
    vectors = {}
    for from_p in scan:
        for to_p in scan:
            vectors[(from_p, to_p)] = vector(from_p, to_p)

    return vectors

def vector_overlap(vectors_a, vectors_b):
    ac = Counter(vectors_a)
    bc = Counter(vectors_b)

    vectors = []   
    for i in set(vectors_a).intersection(vectors_b):
        vectors.extend([i] * min(ac[i], bc[i]))
    return len(vectors) >= 144

def overlap(distances_a, distances_b):
    ac = Counter(distances_a)
    bc = Counter(distances_b)

    numbers = []   
    for i in set(distances_a).intersection(distances_b):
        numbers.extend([i] * min(ac[i], bc[i]))
    return len(numbers) >= 66

def rotate_over_x(scan):
    rotated_scan = []

    for point in scan:
        x, y, z = point
        rotated_scan.append((x, -z, y))

    return rotated_scan

def rotate_over_y(scan):
    rotated_scan = []

    for point in scan:
        x, y, z = point
        rotated_scan.append((z, y, -x))

    return rotated_scan

def rotate_over_z(scan):
    rotated_scan = []

    for point in scan:
        x, y, z = point
        rotated_scan.append((-y, x, z))

    return rotated_scan

def get_rotations(scan):
    rotated_scans = []
    
    for _ in range(4):
        scan = rotate_over_y(scan)

        for _ in range(4):
            scan = rotate_over_z(scan)
            rotated_scans.append(scan)

    scan = rotate_over_x(scan)

    for _ in range(4):
        scan = rotate_over_z(scan)
        rotated_scans.append(scan)

    for _ in range(2):
        scan = rotate_over_y(scan)

    for _ in range(4):
        scan = rotate_over_z(scan)
        rotated_scans.append(scan)

    return rotated_scans
    
# read in scans
scans = []
idx = -1
for line in input:
    if len(line) == 0:
        continue
    elif 'scanner' in line:
        idx += 1
        scans.append([])
    else:
        x, y, z = line.split(',')
        scans[idx].append((int(x), int(y), int(z)))

# calculate distances in scan
distances = []
idx = -1
for scan in scans:
    temp_scan = scan[:]
    idx += 1
    distances.append([])
    for point_a in scan:
        temp_scan.remove(point_a)
        for point_b in temp_scan:
            distances[idx].append(distance(point_a, point_b))
    
# find overlap (12 equal distances)
overlaps = []
idx = -1
for d1 in distances:
    idx += 1
    overlaps.append([])
    idx2 = -1
    for d2 in distances:
        idx2 += 1
        if overlap(d1, d2): overlaps[idx].append(idx2)

for i in range(len(overlaps)):
    overlaps[i].remove(i)

# transform overlaps to same space
added = [0]
sensors = {0: (0,0,0)}
beacons = scans[0][:]

def transform_and_add(current):
    vectors_a = get_vectors(scans[current])
    comp_sensor = sensors[current]

    for idx in [i for i in overlaps[current] if i not in added]:
        for scan in get_rotations(scans[idx]):
            vectors_b = get_vectors(scan)
            if(vector_overlap(vectors_a.values(), vectors_b.values()) and idx not in added):
                go = True
                for k, v in vectors_a.items():
                    for l, u in vectors_b.items():
                        if go and v == u and v != (0,0,0) and list(vectors_a.values()).count(v) == 1 and list(vectors_b.values()).count(u) == 1:
                            from_a, _ = k
                            from_b, _ = l
                            offset_x = from_b[0] - from_a[0]
                            offset_y = from_b[1] - from_a[1]
                            offset_z = from_b[2] - from_a[2]
                            scans[idx] = []
                            for beacon in scan:
                                coor = (beacon[0]-offset_x,beacon[1]-offset_y, beacon[2]-offset_z)
                                beacons.append(coor)
                                scans[idx].append(coor)
                            sensors[idx] = (-offset_x, -offset_y, -offset_z) 

                            go = False
                            

        added.append(idx)
        transform_and_add(idx)

transform_and_add(0)
print('Part 1:', len(set(beacons)))

mann_distances = []

for s1 in sensors.values():
    for s2 in sensors.values():
        mann_distances.append(distance(s1, s2))

print('Part 2:', max(mann_distances))