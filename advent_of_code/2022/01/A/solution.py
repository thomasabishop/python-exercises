test_input = "/home/thomas/repos/advent_of_python/2022/01/input.test.txt"
main_input = "/home/thomas/repos/advent_of_python/2022/01/input.txt"

with open(main_input, "r") as f:
    greatest_total = 0
    running_total = 0

    lines = f.readlines()
    lines = [line.strip() for line in lines]

    i = 0
    for i in range(i, len(lines)):
        if lines[i] == '':
            if running_total > greatest_total:
                greatest_total = running_total
            running_total = 0
            continue
        else:
            running_total += int(lines[i])
    print(greatest_total)
