import functools

with open('input') as f:
    rangeX, rangeY = f.readline()[15:].split(', y=')

minX, maxX = map(int, rangeX.split('..'))
minY = min(list(map(int, rangeY.split('..'))))
maxY = max(list(map(int, rangeY.split('..'))))

target_coors = [(y, x) for x in range(minX, maxX + 1)
                for y in range(minY, maxY + 1)]

highestdY = -minY - 1
print('Part 1:', highestdY * (highestdY + 1) / 2)

hits = 0
for dY in range(minY, highestdY + 1):
    for dX in range(maxX + 1):
        highestY = 0
        currentdY = dY
        currentdX = dX
        currentY = 0
        currentX = 0
        while currentX <= maxX and currentY >= minY:
            currentX = currentX + currentdX
            currentY = currentY + currentdY
            if currentY > highestY:
                highestY = currentY
            if (currentY, currentX) in target_coors:
                hits += 1
                break
            if currentdX > 0:
                currentdX -= 1
            currentdY -= 1

print('Part 2:', hits)
