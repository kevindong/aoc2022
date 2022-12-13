from itertools import zip_longest
from functools import cmp_to_key


def parse_input():
    with open("input.txt", "r") as f:
        data = f.read()
    lines = list(map(lambda x: eval(x), filter(lambda f: f != "", data.split("\n"))))
    return lines


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


lines = parse_input()
lines.extend([[[2]], [[6]]])
lines.sort(key=cmp_to_key(compare))
first = None
second = None
for i, line in enumerate(lines):
    if line == [[2]]:
        first = i + 1
    elif line == [[6]]:
        second = i + 1
print(first * second)
