test_input = "/home/thomas/repos/advent_of_python/2022/01/input.test.txt"
main_input = "/home/thomas/repos/advent_of_python/2022/01/input.txt"

with open(main_input, "r") as f:
    running_total = 0
    totals = []
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    lines.append('')  # super hacky!
    i = 0
    for i in range(i, len(lines)):
        if lines[i] == '':
            totals.append(running_total)
            running_total = 0
            continue
        else:
            running_total += int(lines[i])
    totals.sort(reverse=True)
    highest_three = sum([totals[0], totals[1], totals[2]])

print(highest_three)
