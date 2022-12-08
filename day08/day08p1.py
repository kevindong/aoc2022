with open("input.txt", "r") as f:
    data = f.readlines()
    data = [[int(i) for i in list(d[:-1])] for d in data]

visible_trees = set()

# Fill in top and bottom edge
for i in [0, len(data) - 1]:
    for j in range(len(data[i])):
        visible_trees.add((i, j))

# Fill in left and right edge
for j in [0, len(data[0]) - 1]:
    for i in range(len(data)):
        visible_trees.add((i, j))

print(len(visible_trees))

# Scan top down
for column in range(len(data[0])):
    max_seen = data[0][column]
    for row in range(1, len(data)):
        current = data[row][column]
        if current > max_seen:
            visible_trees.add((row, column))
        max_seen = max(max_seen, current)

# Scan bottom up
for column in range(len(data[0])):
    max_seen = data[len(data) - 1][column]
    for row in range(len(data) - 2, -1, -1):
        current = data[row][column]
        if current > max_seen:
            visible_trees.add((row, column))
        max_seen = max(max_seen, current)

# Scan left to right
for row in range(len(data)):
    max_seen = data[row][0]
    for column in range(1, len(data[row])):
        current = data[row][column]
        if current > max_seen:
            visible_trees.add((row, column))
        max_seen = max(max_seen, current)

# Scan right to left
for row in range(len(data)):
    max_seen = data[row][len(data[row]) - 1]
    for column in range(len(data[row]) - 2, -1, -1):
        current = data[row][column]
        if current > max_seen:
            visible_trees.add((row, column))
        max_seen = max(max_seen, current)

print(len(visible_trees))
