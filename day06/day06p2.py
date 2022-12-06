with open("input.txt", "r") as f:
    data = f.read()
    print([data])

for i in range(14, len(data)):
    substring = data[i - 14 : i]
    if len(set(substring)) == 14:
        print(i)
        break
