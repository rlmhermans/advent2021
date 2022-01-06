import itertools as it
from math import floor

with open('input') as f:
    input = f.read().splitlines()

def execute(program, number):
    variables = {'w': 0, 'x': 0, 'y': 0, 'z': 0}
    for line in program:
        if 'inp' in line:
            variables[line[4]] = number.pop(0)
        else:
            b = variables[line[6:]] if line[6:].isalpha() else int(line[6:])
            if 'add' in line:
                variables[line[4]] += b
            elif 'mul' in line:
                variables[line[4]] *= b
            elif 'div' in line:
                variables[line[4]] = floor(variables[line[4]] / b)
            elif 'mod' in line:
                variables[line[4]] %= b
            elif 'eql' in line:
                variables[line[4]] = 1 if variables[line[4]] == b else 0

    return variables

program = input[0:1]
valid_highs = []

for line in input[1:]:
    if 'inp' in line:
        for x in range(9,0,-1):
            variables = execute(program, valid_highs + [x])
            if variables['z'] == 0: 
                valid_highs.append(x)
                break
    
    program.append(line)

for x in range(9,0,-1):
            variables = execute(program, valid_highs + [x])
            if variables['z'] == 0: 
                valid_highs.append(x)
                break

print(valid_highs)