with open("input.txt", "r") as f:
    data = f.readlines()
    data = [d[:-1] for d in data]


def update_output(outputs, cycle, register):
    if len(outputs) == 0:
        outputs.append([])
    if register - 1 <= ((cycle % 40) - 1) <= register + 1:
        outputs[-1].append("#")
    else:
        outputs[-1].append(".")

    if cycle % 40 == 0:
        outputs.append([])


cycle = 1
register = 1
outputs = []
for line in data:
    if line == "noop":
        update_output(outputs, cycle, register)
        cycle += 1
        continue
    [command, operand] = line.split(" ")
    operand = int(operand)
    assert command == "addx"
    update_output(outputs, cycle, register)
    cycle += 1
    update_output(outputs, cycle, register)
    register += operand
    cycle += 1

print(cycle)
print(register)
outputs.pop()
print(outputs)

for l in outputs:
    print("".join(l))
