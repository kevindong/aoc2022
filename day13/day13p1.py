from itertools import zip_longest


def parse_input():
    with open("input.txt", "r") as f:
        data = f.read()
    pairs = data.split("\n\n")
    pairs = [list(map(eval, pair.split("\n"))) for pair in pairs]
    return pairs


def compare(left, right):
    if left is None:
        return -1
    elif right is None:
        return 1
    elif isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        elif left == right:
            return 0
        else:
            return 1
    elif isinstance(left, int) and isinstance(right, list):
        return compare([left], right)
    elif isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])
    else:
        for l, r in zip_longest(left, right):
            result = compare(l, r)
            if result == 0:
                continue
            return result
        return 0


pairs = parse_input()
# print(pairs)
index_sum = 0
for i, (left, right) in enumerate(pairs):
    result = compare(left, right)
    print(f"{i+1}: {result}")
    if result == -1:
        index_sum += i + 1
print(index_sum)
