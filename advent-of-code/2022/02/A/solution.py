test_input = "/home/thomas/repos/advent_of_python/2022/02/input.test.txt"
main_input = "/home/thomas/repos/advent_of_python/2022/02/input.txt"

lookup_score = {
    'AX': 4,
    'AY': 8,
    'AZ': 3,
    'BX': 1,
    'BY': 5,
    'BZ': 9,
    'CX': 7,
    'CY': 2,
    'CZ': 6
}

total_score = 0

with open(main_input, "r") as f:
    line = f.readline()
    while line:
        line = line.strip().replace(" ", "")
        total_score += lookup_score[line]
        line = f.readline()
    print(total_score)
