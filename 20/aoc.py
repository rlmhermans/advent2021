import numpy as np

with open('input') as f:
    algo, _, *image = f.read().splitlines()

def conv(x): return 1 if x == '#' else 0

image = [list(map(conv, line)) for line in [list(line) for line in image]]
m = np.matrix(image)
pad_with = 0

for _ in range(0, 50):
    m = np.pad(m, 2, constant_values=pad_with)
    pad_with = conv(algo[0]) if pad_with == 0 else conv(algo[511])
    output = np.copy(m)
    width = len(output)
    for y in range(1, width-1):
        for x in range(1, width-1):
            sbin = '' + str(m[y-1, x-1]) + str(m[y-1, x]) + str(m[y-1, x+1]) + str(m[y, x-1]) + str(m[y, x]) + str(m[y, x+1]) + str(m[y+1, x-1]) + str(m[y+1, x]) + str(m[y+1, x+1]) 
            output[y, x] = conv(algo[int(sbin, 2)])

    m = output[1:-1, 1:-1]
    

print(np.sum(m))