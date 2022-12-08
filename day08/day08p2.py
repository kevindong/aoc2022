with open("input.txt", "r") as f:
    data = f.readlines()
    data = [[int(i) for i in list(d[:-1])] for d in data]


def scan_up(data, i, j):
    if i == 0:
        return 0
    score = 0
    start_height = data[i][j]
    for i in range(i - 1, -1, -1):
        current_height = data[i][j]
        score += 1
        if current_height >= start_height:
            break
    return score


def scan_down(data, i, j):
    if i == len(data) - 1:
        return 0
    score = 0
    start_height = data[i][j]
    for i in range(i + 1, len(data)):
        current_height = data[i][j]
        score += 1
        if current_height >= start_height:
            break
    return score


def scan_left(data, i, j):
    if j == 0:
        return 0
    score = 0
    start_height = data[i][j]
    for j in range(j - 1, -1, -1):
        current_height = data[i][j]
        score += 1
        if current_height >= start_height:
            break
    return score


def scan_right(data, i, j):
    if j == 0:
        return 0
    score = 0
    start_height = data[i][j]
    for j in range(j + 1, len(data[0])):
        current_height = data[i][j]
        score += 1
        if current_height >= start_height:
            break
    return score


max_score = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        current_score = (
            scan_left(data, i, j)
            * scan_right(data, i, j)
            * scan_up(data, i, j)
            * scan_down(data, i, j)
        )
        max_score = max(max_score, current_score)
print(max_score)
