with open("input.txt", "r") as f:
    data = f.readlines()

total = 0

mapping = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
}

reverse_mapping = {
    "rock": "A",
    "paper": "B",
    "scissors": "C",
}

points = {
    "A": 1,
    "B": 2,
    "C": 3,
}

losing = {
    "rock": "paper",
    "paper": "scissors",
    "scissors": "rock",
}

winning = {
    "paper": "rock",
    "scissors": "paper",
    "rock": "scissors",
}

for game in data:
    game = game[:-1]
    game = game.split(" ")
    them = mapping[game[0]]
    me = game[1]

    game_score = 0

    if me == "X":  # lose
        game_score += 0
        game_score += points[reverse_mapping[winning[them]]]
    elif me == "Y":  # draw
        game_score += 3
        game_score += points[reverse_mapping[them]]
    else:  # win
        game_score += 6
        game_score += points[reverse_mapping[losing[them]]]

    print(game_score)
    total += game_score

print(total)
