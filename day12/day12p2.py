import collections


def parse_board():
    with open("input.txt", "r") as f:
        data = f.readlines()
    output = []
    start = None
    end = None
    for row, line in enumerate(data):
        output.append([])
        for column, c in enumerate(line):
            if c == "\n":
                continue
            elif c == "S":
                output[-1].append(ord("a"))
                start = (row, column)
            elif c == "E":
                output[-1].append(ord("z"))
                end = (row, column)
            else:
                output[-1].append(ord(c))
    return (output, start, end)


def append_adjacent(board, steps, x, y, seen):
    output = []
    movements = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for (dx, dy) in movements:
        new_x, new_y = x + dx, y + dy
        if (new_x, new_y) in seen:
            continue
        elif not (0 <= new_x < len(board)) or not (0 <= new_y < len(board[0])):
            continue
        old_height = board[x][y]
        new_height = board[new_x][new_y]
        if steps[new_x][new_y] is None and new_height - old_height <= 1:
            output.append((new_x, new_y, steps[x][y] + 1))
            seen.add((new_x, new_y))
    return output


def compute_fewest_steps(board, start, end):
    steps = [[None for _ in range(len(board[0]))] for _ in range(len(board))]
    steps[start[0]][start[1]] = 0
    queue = collections.deque()
    seen = set()
    queue.append((start[0], start[1]))
    while len(queue) > 0:
        (x, y) = queue.popleft()
        new_nodes = append_adjacent(board, steps, x, y, seen)
        for (new_x, new_y, new_steps) in new_nodes:
            if (new_x, new_y) == end:
                return new_steps
            steps[new_x][new_y] = new_steps
            queue.append((new_x, new_y))
    return len(board) * len(board[1])


board, start, end = parse_board()
min_steps = compute_fewest_steps(board, start, end)
for i, row in enumerate(board):
    for j, height in enumerate(row):
        if height == ord("a"):
            result = compute_fewest_steps(board, (i, j), end)
            min_steps = min(min_steps, result)
print(min_steps)
