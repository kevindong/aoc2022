with open("input.txt", "r") as f:
    data = f.readlines()

total = 0

for game in data:
    game = game[:-1]
    game = game.split(" ")
    them = game[0]
    me = game[1]

    game_score = 0

    if me == "X":
        game_score += 1
    elif me == "Y":
        game_score += 2
    else:
        game_score += 3

    if (
        (them == "A" and me == "X")
        or (them == "B" and me == "Y")
        or (them == "C" and me == "Z")
    ):
        game_score += 3
    elif them == "A" and me == "Y":
        game_score += 6
    elif them == "B" and me == "Z":
        game_score += 6
    elif them == "C" and me == "X":
        game_score += 6
    else:
        game_score += 0

    print(game_score)
    total += game_score

print(total)
