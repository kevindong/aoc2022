with open("input.txt", "r") as f:
    data = f.readlines()

summation = 0
for i in range(0, len(data), 3):
    grouping = data[i : i + 3]
    print(grouping)
    for i in range(3):
        grouping[i] = grouping[i][:-1]

    common = (
        set(grouping[0]).intersection(set(grouping[1])).intersection(set(grouping[2]))
    )
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
