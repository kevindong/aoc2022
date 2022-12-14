def parse_input():
    with open("input.txt", "r") as f:
        data = f.readlines()
    paths = [line[:-1] for line in data]
    output_paths = []
    x_range = [500, 500]
    y_range = [0, 0]
    for path in paths:
        output_path = []
        key_points = path.split(" -> ")
        for key_point in key_points:
            [x, y] = key_point.split(",")
            x = int(x)
            y = int(y)
            x_range = [min(x_range[0], x), max(x_range[1], x)]
            y_range = [min(y_range[0], y), max(y_range[1], y)]
            output_path.append([x, y])
        output_paths.append(output_path)
    return output_paths, x_range, y_range


def generate_grid(paths, x_range, y_range):
    grid = [["." for _ in range(x_range[1] + 1)] for _ in range(y_range[1] + 1)]
    # print(grid)
    for path in paths:
        # print(path)
        for i in range(1, len(path)):
            # print("key point")
            prior = path[i - 1]
            current = path[i]
            dx, dy = current[0] - prior[0], current[1] - prior[1]
            if dx > 0:
                dx = 1
            elif dx < 0:
                dx = -1
            elif dy > 0:
                dy = 1
            elif dy < 0:
                dy = -1
            if (dx == 0 and dy == 0) or (dx != 0 and dy != 0):
                assert False
            while prior != current:
                # print(prior)
                grid[prior[1]][prior[0]] = "#"
                prior[0] += dx
                prior[1] += dy
            grid[prior[1]][prior[0]] = "#"
        # print("done")
    return grid


def count_falling_sand(grid, x_range, y_range):
    units_of_sand_resting = 0
    while True:
        x = 500
        y = -1
        while True:
            # if not x_range[0] <= x <= x_range[1] or not 0 <= y <= y_range[1]:
            #     return units_of_sand_resting
            if y + 1 > y_range[1]:
                return units_of_sand_resting
            elif grid[y + 1][x] == ".":  # directly below
                y += 1
            elif x - 1 < x_range[0]:
                return units_of_sand_resting
            elif grid[y + 1][x - 1] == ".":  # bottom-left
                y += 1
                x -= 1
            elif x + 1 > x_range[1]:
                return units_of_sand_resting
            elif grid[y + 1][x + 1] == ".":  # bottom-right
                y += 1
                x += 1
            else:
                grid[y][x] = "o"
                units_of_sand_resting += 1
                break
    assert False


(paths, x_range, y_range) = parse_input()
grid = generate_grid(paths, x_range, y_range)
for row in grid:
    print("".join(row[x_range[0] :]))
sand = count_falling_sand(grid, x_range, y_range)
print(sand)
for row in grid:
    print("".join(row[x_range[0] :]))
