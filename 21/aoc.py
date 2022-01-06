from collections import defaultdict

d = defaultdict(tuple)

def game(player_1_points, player_2_points, player_1_turn, roll_points, roll, player_1_pos, player_2_pos):
    if (player_1_points, player_2_points, player_1_turn, roll_points, roll, player_1_pos, player_2_pos) in d:
        return d[(player_1_points, player_2_points, player_1_turn, roll_points, roll, player_1_pos, player_2_pos)]

    wins = [0,0]

    if roll == 3:
        if player_1_turn: 
            player_1_pos += roll_points
            player_1_pos %= 10
            if player_1_pos == 0: player_1_pos = 10
            player_1_points += player_1_pos
        else: 
            player_2_pos += roll_points
            player_2_pos %= 10
            if player_2_pos == 0: player_2_pos = 10
            player_2_points += player_2_pos

        roll = 0
        roll_points = 0
        player_1_turn = not player_1_turn

        if player_1_points >= 21: wins[0] += 1
        elif player_2_points >= 21: wins[1] += 1

    if player_1_points < 21 and player_2_points < 21:
        for i in range(1, 4):
            player_1_wins, player_2_wins = game(player_1_points, player_2_points, player_1_turn, i + roll_points, roll+1, player_1_pos, player_2_pos)
            wins[0] += player_1_wins
            wins[1] += player_2_wins

    d[(player_1_points, player_2_points, player_1_turn, roll_points, roll, player_1_pos, player_2_pos)] = wins
    return wins

total_wins = [0, 0]
for i in range(1, 4):
    player_1_wins, player_2_wins = game(0, 0, True, i, 1, 7, 10)
    total_wins[0] += player_1_wins
    total_wins[1] += player_2_wins

print('Part 2:', total_wins)