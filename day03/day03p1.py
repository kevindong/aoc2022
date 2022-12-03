with open("input.txt", "r") as f:
    data = f.readlines()

summation = 0
for rucksack in data:
    rucksack = rucksack[:-1]
    print(rucksack)
    length = len(rucksack)
    first = rucksack[: length // 2]
    second = rucksack[length // 2 :]
    print((first, second))
    first = set(first[::1])
    second = set(second[::1])
    common = first.intersection(second)
    print(common)
    assert len(common) == 1

    common = list(common)[0]
    value = 0
    if ord("a") <= ord(common) <= ord("z"):
        value = ord(common) - ord("a") + 1
    else:
        value = ord(common) - ord("A") + 1 + 26
    print(value)
    summation += value

print(summation)
