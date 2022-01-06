with open('input') as f:
    input = f.read().splitlines()

OPPOSITES = {'}': '{', ']': '[', ')': '(', '>': '<'}
OPPOSITES_2 = {y:x for x,y in OPPOSITES.items()}
POINTS = {'}': 1197, ']': 57, ')': 3, '>': 25137}
POINTS_2 = {'}': 3, ']': 2, ')': 1, '>': 4}

score = 0
scores = []

for line in input:
    stack = []
    corrupt = False

    for char in line:
        if char in ['[', '(', '{', '<']:
            stack.append(char)

        else:
            opp = stack.pop()
            if OPPOSITES[char] is not opp:
                score += POINTS[char]
                corrupt = True
                break


    if not corrupt:
        stack.reverse()

        score_2 = 0

        for item in stack:
            score_2 *= 5
            score_2 += POINTS_2[OPPOSITES_2[item]]

        scores.append(score_2)

scores.sort()
print('Part 1:', score)
print('Part 2:', scores[round(len(scores)/2)])