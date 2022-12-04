with open("input.txt", "r") as f:
    data = f.readlines()
    data = list(map(lambda d: d.replace("\n", ""), data))


def get_ranges(elf):
    a, b = elf.split("-")
    return (int(a), int(b))


def does_contain(a, b):
    if a[0] <= b[0] <= a[1] and a[0] <= b[1] <= a[1]:
        return True
    elif b[0] <= a[0] <= b[1] and b[0] <= a[1] <= b[1]:
        return True
    return False


counter = 0
for grouping in data:
    elves = grouping.split(",")
    assert len(elves) == 2
    one = get_ranges(elves[0])
    two = get_ranges(elves[1])
    if does_contain(one, two):
        counter += 1
print(counter)
