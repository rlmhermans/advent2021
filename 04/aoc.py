with open('input') as f:
    input = f.read().splitlines()

def transpose(array):
    return [[array[j][i] for j in range(len(array))] for i in range(len(array[0]))]

numbers = input[0].split(',')
cards = []
card = []
input.pop(0)
input.pop(0)

for line in input:
    line = line.strip().replace('  ', ',').replace(' ', ',').split(',')

    if len(line) == 1:
        card += transpose(card)
        cards.append(card)
        card = []
    else:
        card.append(line)

card += transpose(card)
cards.append(card)

drawn = set()
cards_won = []
for number in numbers:
    drawn.add(number)

    for card in cards:
        if card not in cards_won:
            for row in card:
                if set(row).issubset(drawn):
                    card_numbers = [int(card[i][j]) for j in range(5) for i in range(5) if card[i][j] not in drawn]
                    print(sum(card_numbers) * int(number))
                    cards_won.append(card)