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
    grid = [["." for _ in range(x_range[1] + 1000)] for _ in range(y_range[1] + 3)]
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
    sand_deposited_min_x = 500
    sand_deposited_max_x = 500
    while True:
        x = 500
        y = -1
        while True:
            # if not x_range[0] <= x <= x_range[1] or not 0 <= y <= y_range[1]:
            #     return units_of_sand_resting
            if grid[0][500] == "o":
                return units_of_sand_resting, [
                    sand_deposited_min_x,
                    sand_deposited_max_x,
                ]
            elif y == y_range[1] + 1:
                units_of_sand_resting += 1
                x_location = None
                if grid[y][x] == ".":
                    x_location = x
                    grid[y][x] = "o"
                elif grid[y][x - 1] == ".":
                    x_location = x - 1
                    grid[y][x - 1] = "o"
                elif grid[y][x + 1] == ".":
                    x_location = x + 1
                    grid[y][x + 1] = "o"
                sand_deposited_min_x = min(sand_deposited_min_x, x_location)
                sand_deposited_max_x = max(sand_deposited_max_x, x_location)
                break
            elif grid[y + 1][x] == ".":  # directly below
                y += 1
            elif grid[y + 1][x - 1] == ".":  # bottom-left
                y += 1
                x -= 1
            elif grid[y + 1][x + 1] == ".":  # bottom-right
                y += 1
                x += 1
            else:
                grid[y][x] = "o"
                units_of_sand_resting += 1
                sand_deposited_min_x = min(sand_deposited_min_x, x)
                sand_deposited_max_x = max(sand_deposited_max_x, x)
                break
    assert False


(paths, x_range, y_range) = parse_input()
grid = generate_grid(paths, x_range, y_range)
for row in grid:
    print("".join(row[x_range[0] : x_range[1] + 1]))
[sand, [min_x, max_x]] = count_falling_sand(grid, x_range, y_range)
for row in grid:
    print("".join(row[min_x : max_x + 1]))
