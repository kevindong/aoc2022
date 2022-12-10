with open("input.txt", "r") as f:
    data = f.readlines()
    data = [d[:-1] for d in data]


def is_interesting_cycle(cycle):
    return cycle in [20, 60, 100, 140, 180, 220]


cycle = 1
register = 1
signals_strengths = []
for line in data:
    if line == "noop":
        cycle += 1
        if is_interesting_cycle(cycle):
            signals_strengths.append(cycle * register)
        continue
    [command, operand] = line.split(" ")
    operand = int(operand)
    assert command == "addx"
    if is_interesting_cycle(cycle + 1):
        signals_strengths.append((cycle + 1) * register)
    elif is_interesting_cycle(cycle + 2):
        signals_strengths.append((cycle + 2) * (register + operand))
    register += operand
    cycle += 2

print(cycle)
print(register)
print(signals_strengths)
print(sum(signals_strengths))
