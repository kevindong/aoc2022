with open("input.txt", "r") as f:
    data = f.readlines()
    data = [d[:-1] for d in data]

moves = []
for line in data:
    direction, units = line.split(" ")
    units = int(units)
    assert units > 0
    if direction == "L":
        moves.append((-1, 0, units))
    elif direction == "R":
        moves.append((1, 0, units))
    elif direction == "U":
        moves.append((0, 1, units))
    elif direction == "D":
        moves.append((0, -1, units))
    else:
        assert False


def move_tail(current_head, current_tail):
    (hx, hy) = current_head
    (tx, ty) = current_tail
    dx, dy = hx - tx, hy - ty
    if dx == 0 and dy == 0:
        print("No move")
        return current_tail
    elif dx >= 1 and dy == 0:  # Move right
        return (tx + 1, ty)
    elif dx <= -1 and dy == 0:  # Move left
        return (tx - 1, ty)
    elif dx == 0 and dy >= 1:  # Move up
        return (tx, ty + 1)
    elif dx == 0 and dy <= -1:  # Move down
        return (tx, ty - 1)
    elif dx >= 1 and dy >= 1:  # Move top-right corner
        return (tx + 1, ty + 1)
    elif dx >= 1 and dy <= -1:  # Move bottom-right corner
        return (tx + 1, ty - 1)
    elif dx <= -1 and dy >= 1:  # Move top-left corner
        return (tx - 1, ty + 1)
    elif dx <= -1 and dy <= -1:  # Move bottom-left corner
        return (tx - 1, ty - 1)
    else:
        print("Not bordering")
        assert False


def is_adjacent(head, tail):
    (hx, hy) = head
    (tx, ty) = tail
    dx, dy = abs(hx - tx), abs(hy - ty)
    return dx <= 1 and dy <= 1


places_visited = set()
places_visited.add((0, 0))
knots = [(0, 0) for _ in range(10)]
for (dx, dy, units) in moves:
    for _ in range(units):
        knots[0] = (knots[0][0] + dx, knots[0][1] + dy)
        for i in range(1, len(knots)):
            head = knots[i - 1]
            tail = knots[i]
            while not is_adjacent(head, tail):
                tail = move_tail(head, tail)
                if i == 9:
                    places_visited.add(tail)
            knots[i] = tail
print(len(places_visited))
# print(places_visited)
