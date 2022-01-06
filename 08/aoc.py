with open('input') as f:
    input = f.read().splitlines()

total = 0

for line in input:
    digits = {x:'' for x in range(10)}
    patterns = line.split(' | ')[0].split(' ')
    code = line.split(' | ')[1].split(' ')

    for pattern in patterns:
        if len(pattern) == 2: digits[1] = pattern
        elif len(pattern) == 3: digits[7] = pattern
        elif len(pattern) == 4: digits[4] = pattern
        elif len(pattern) == 7: digits[8] = pattern

    p = set(digits[4]) - set(digits[1])

    for pattern in patterns:
        if len(pattern) == 5:
            if set(digits[1]).issubset(pattern):
                digits[3] = pattern
            elif set(p).issubset(pattern):
                digits[5] = pattern
            else:
                digits[2] = pattern

        elif len(pattern) == 6:
            if not set(digits[1]).issubset(pattern):
                digits[6] = pattern
            elif not set(digits[4]).issubset(pattern):
                digits[0] = pattern
            else:
                digits[9] = pattern


    number = ''
    for c in code:
        for k,v in digits.items():
            if set(v) == set(c):
                number += str(k)
    total += int(number)

print('Part 2:', total)