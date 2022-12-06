with open("input.txt", "r") as f:
    data = f.read()
    print([data])

for i in range(4, len(data)):
    substring = data[i - 4 : i]
    if len(set(substring)) == 4:
        print(i)
        break
