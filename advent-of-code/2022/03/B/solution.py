# Split input lines into groups of three, find the one char that is common to all three
# Run through char lookup function again and sum

import string
test_input = "/home/thomas/repos/advent_of_python/2022/03/input.test.txt"
main_input = "/home/thomas/repos/advent_of_python/2022/03/input.txt"


def get_char_value(lookup):
    alpha_values = list(string.ascii_lowercase) + list(string.ascii_uppercase)
    return alpha_values.index(lookup) + 1


with open(main_input, "r") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

    triads = []

    for i in range(0, len(lines), 3):  # make note of the step value here
        triads.append(lines[i: i + 3])

    common_chars = []
    for group in triads:
        for char in group[0]:
            if char in group[1] and char in group[2]:
                common_chars.append(get_char_value(char))
                break  # I wasn't breaking that was the problem
    print(sum(common_chars))
