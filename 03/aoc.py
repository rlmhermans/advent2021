with open('input') as f:
    input = f.read().splitlines()

def calc_rate(input, test):
    transposed = [[int(input[j][i]) for j in range(len(input))] for i in range(len(input[0]))]

    rate = ''

    for bit in transposed:
        rate += '1' if test(bit) else '0'

    return rate

def gamma_test(x): return sum(x) >= len(x)/2
def epsilon_test(x): return sum(x) < len(x)/2

gamma_rate = calc_rate(input, gamma_test)
epsilon_rate = calc_rate(input, epsilon_test)

print('Part 1: ', int(gamma_rate, 2) * int(epsilon_rate, 2))

def find_rating(input, test):
    diagnostics = list(input)

    for i in range(len(diagnostics[0])):
        rate = calc_rate(diagnostics, test)
        diagnostics = [x for x in diagnostics if x[i] in rate[i]]

        if len(diagnostics) == 1:
            return int(diagnostics[0], 2)

oxygen = find_rating(input, gamma_test)
scrubber = find_rating(input, epsilon_test)

print('Part 2: ', oxygen * scrubber)