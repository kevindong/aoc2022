def parse_start_positions(start_positions):
    start_positions = start_positions[:-1]
    row_width = len(start_positions[0]) + 1
    assert row_width % 4 == 0
    stack_count = row_width // 4
    stacks = [[] for _ in range(stack_count)]
    for row in start_positions:
        for i in range(1, len(row), 4):
            if row[i] == " ":
                continue
            stacks[i // 4].append(row[i])
    for i in range(len(stacks)):
        stacks[i] = stacks[i][::-1]
    return stacks


def move_crates(stacks, moves):
    for [_, quantity, _, start_stack, _, end_stack] in map(
        lambda x: x.split(" "), moves
    ):
        quantity = int(quantity)
        start_stack_index = int(start_stack) - 1
        end_stack_index = int(end_stack) - 1
        stacks[end_stack_index].extend(
            stacks[start_stack_index][len(stacks[start_stack_index]) - quantity :]
        )
        stacks[start_stack_index] = stacks[start_stack_index][:-quantity]
    return stacks


with open("input.txt", "r") as f:
    data = f.read()

data = data.split("\n\n")
assert len(data) == 2

[start_positions, moves] = data

start_positions = start_positions.split("\n")
stacks = parse_start_positions(start_positions)
print(f"Stacks: {stacks}")

moves = moves.split("\n")
move_crates(stacks, moves)

output = ""
for stack in stacks:
    if len(stack) == 0:
        continue
    output += stack[-1]
print(output)
