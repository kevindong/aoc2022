def add_file(fs, path, file_name, size):
    working_directory = fs
    if len(path) == 0:
        fs[file_name] = size
        return
    for i, directory in enumerate(path):
        if directory not in working_directory:
            working_directory[directory] = {}
        if i == len(path) - 1:  # Last directory
            working_directory[directory][file_name] = size
        else:
            working_directory = working_directory[directory]


def add_directory(fs, path, new_directory):
    working_directory = fs
    for i, directory in enumerate(path):
        if directory not in working_directory:
            working_directory[directory] = {}
        if i == len(path) - 1:
            working_directory[directory][new_directory] = working_directory[
                directory
            ].get(new_directory, {})
        working_directory = working_directory[directory]


def parse_fs():
    with open("input.txt", "r") as f:
        data = f.readlines()
        data = [line[:-1] for line in data]
    current = []
    fs = {}
    i = 0
    while i < len(data):
        line = data[i]
        # print(line)
        if line.startswith("$"):
            components = line.split(" ")
            command = components[1]
            if command == "cd":
                assert len(components) == 3
                path = components[2]
                if path == "/":
                    current = []
                elif path == "..":
                    current.pop()
                else:
                    current.append(path)
            elif command == "ls":
                while i + 1 < len(data) and data[i + 1][0] != "$":
                    i += 1
                    inner_components = data[i].split(" ")
                    assert len(inner_components) == 2
                    if inner_components[0] == "dir":
                        add_directory(fs, current, inner_components[1])
                    else:
                        [size, file_name] = inner_components
                        add_file(fs, current, file_name, int(size))
            else:
                assert False
        i += 1
    # import json
    # print(json.dumps(fs))
    return fs


def find_dirs(current_location, pointer):
    output_dirs = []

    root_value = dfs_sum(pointer)
    output_dirs.append((current_location, root_value))

    for key, value in pointer.items():
        if isinstance(value, dict):
            output_dirs.extend(find_dirs(f"{current_location}/{key}", value))

    return output_dirs


def dfs_sum(pointer):
    running_sum = 0
    for key, value in pointer.items():
        if isinstance(value, int):
            running_sum += value
        else:  # we're at a directory
            running_sum += dfs_sum(value)
    return running_sum


fs = parse_fs()
result = find_dirs("", fs)
result.sort(key=lambda x: x[1])
print(result)

total_available = 70000000
need_unused = 30000000
used = result[-1][1]
unused = total_available - used
delete_target = need_unused - unused
print(delete_target)
for (dir, size) in result:
    if size >= delete_target:
        print((dir, size))
        break
