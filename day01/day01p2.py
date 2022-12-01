with open("input.txt", "r") as f:
    data = f.read()

data = data.split("\n\n")
print(data)
maximums = []
for elf in data:
    values = elf.split("\n")
    value = list(map(int, values))
    maximums.append(sum(value))
maximums.sort(reverse=True)
print(sum(maximums[:3]))
