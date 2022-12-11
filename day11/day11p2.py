import collections
import math
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
        self.items = collections.deque(
            map(int, starting_items_line.split(": ")[1].split(", "))
        )
        self.test_mod = int(test_line.split(" by ")[1])
        self.if_true_monkey = int(if_true_line.split(" monkey ")[1])
        self.if_false_monkey = int(if_false_line.split(" monkey ")[1])

        operation = operation_line.split("new = ")[1]
        if operation == "old * old":
            self.operation = self.exponent
        elif "+" in operation:
            self.operation = self.add
            self.value = int(operation.split(" ")[-1])
        elif "*" in operation:
            self.operation = self.multiply
            self.value = int(operation.split(" ")[-1])

    def exponent(self, worry):
        return worry * worry

    def add(self, worry):
        return worry + self.value

    def multiply(self, worry):
        return worry * self.value

    def __repr__(self):
        return f"Monkey({self.i})"

    # Returns a set of tuples of arity 3 where (worry_level, destination_monkey)
    def inspect_items(self, mod_product):
        out = []
        while len(self.items) > 0:
            item = self.items.popleft()
            worry = self.operation(item)
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
