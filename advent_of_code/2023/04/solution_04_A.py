import os

puzzle_input_path = os.path.join(os.path.dirname(__file__), "data/input.txt")


def parse_ints(line):
    return [int(i) for i in line[line.index(":") + 1 :].split() if i.isnumeric()]


def double(times):
    if times == 1:
        return 1
    else:
        prev = double(times - 1)
        return prev + prev


with open(puzzle_input_path, "r") as f:
    total = 0
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    for line in lines:
        values = parse_ints(line)
        values.sort()
        count = 0
        i = 0
        j = 0 + 1
        while j <= len(values) - 1:
            if values[i] == values[j]:
                count += 1
            i, j = i + 1, j + 1
        if count > 0:
            total += double(count)
    print(total)
