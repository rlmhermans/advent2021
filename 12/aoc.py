from collections import defaultdict
import itertools as it

with open('input') as f:
    input = f.read().splitlines()

edges = defaultdict(list)

for line in input:
    left = line.split('-')[0]
    right = line.split('-')[1]

    edges[left].append(right)
    edges[right].append(left)

paths = []
smaller_caves = [cave for cave in edges.keys() if cave.islower() and cave not in ['start', 'end']]

def visit(vertice, path, twice_allowed):
    path.append(vertice)

    if 'end' in vertice:
        paths.append(path)
    
    else:
        for next_vertice in edges[vertice]:
            if next_vertice in path and next_vertice in twice_allowed:
                visit(next_vertice, path[:], 'none')
            elif not next_vertice.islower() or next_vertice not in path:
                visit(next_vertice, path[:], twice_allowed)

visit('start', [], 'none')
print('Part 1:', len(paths))

for cave in smaller_caves:
    visit('start', [], cave)

paths.sort()
unique_paths = list(paths for paths,_ in it.groupby(paths))
print('Part 2:', len(unique_paths))