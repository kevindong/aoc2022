"""
I had originally done some optimizations for Part 2:
* Used `collections.deque` to make popping from the left side of each monkey's items more efficient
* Using function pointers rather than evals
* Using `math.pow` rather than `value * value`; although this ran into overflow issues

But then I realized the dominating factor is that multiplying very large values is the limiting factor and then that led me stumbling onto the number theory trick to speed things up. For simplicity, I reverted this file back to what it was for Part 1, but with the number theory trick retained. The optimizations I made definitely made a difference, but even without those (and with just the number theory trick), this program still completes within a few seconds and I like the simplicity of this approach more.
"""

import functools


class Monkey:
    def __init__(
        self,
        i,
        starting_items_line,
        operation_line,
        test_line,
        if_true_line,
        if_false_line,
    ):
        self.i = i
        self.items = list(map(int, starting_items_line.split(": ")[1].split(", ")))
        self.operation = operation_line.split("new = ")[1]
        self.test_mod = int(test_line.split(" by ")[1])
        self.if_true_monkey = int(if_true_line.split(" monkey ")[1])
        self.if_false_monkey = int(if_false_line.split(" monkey ")[1])

    def __repr__(self):
        return f"Monkey({self.i})"

    # Returns a set of tuples of arity 3 where (worry_level, destination_monkey)
    def inspect_items(self, mod_product):
        out = []
        while len(self.items) > 0:
            item = self.items.pop(0)
            worry = eval(self.operation, None, {"old": item})
            worry %= mod_product
            if worry % self.test_mod == 0:
                out.append((worry, self.if_true_monkey))
            else:
                out.append((worry, self.if_false_monkey))
        return out


def parse_monkeys():
    with open("input.txt", "r") as f:
        monkeys = f.read().split("\n\n")
    out = []
    for i, monkey in enumerate(monkeys):
        [
            _,
            starting_items_line,
            operation_line,
            test_line,
            if_true_line,
            if_false_line,
        ] = monkey.split("\n")
        out.append(
            Monkey(
                i,
                starting_items_line,
                operation_line,
                test_line,
                if_true_line,
                if_false_line,
            )
        )
    return out


def count_inspections(monkeys, rounds):
    counts = {}
    mod_product = functools.reduce(
        lambda x, y: x * y, map(lambda m: m.test_mod, monkeys), 1
    )
    for i in range(rounds):
        for monkey in monkeys:
            counts[monkey.i] = counts.get(monkey.i, 0) + len(monkey.items)
            items = monkey.inspect_items(mod_product)
            for (worry_level, destination_monkey) in items:
                monkeys[destination_monkey].items.append(worry_level)
    return counts


monkeys = parse_monkeys()
counts = count_inspections(monkeys, 10000)
sorted_counts = sorted(counts.items(), key=lambda t: t[1], reverse=True)
monkey_business_level = sorted_counts[0][1] * sorted_counts[1][1]
print(monkey_business_level)
