with open("input.txt", "r") as f:
    data = f.read()

data = data.split("\n\n")
print(data)
maximum = 0
for elf in data:
    values = elf.split("\n")
    value = map(int, values)
    maximum = max(sum(value), maximum)
print(maximum)
