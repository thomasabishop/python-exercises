import string
test_input = "/home/thomas/repos/advent_of_python/2022/03/input.test.txt"
main_input = "/home/thomas/repos/advent_of_python/2022/03/input.txt"


def get_char_value(lookup):
    alpha_values = list(string.ascii_lowercase) + list(string.ascii_uppercase)
    return alpha_values.index(lookup) + 1


with open(main_input, "r") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

    total_sum = 0

    for line in lines:
        segment_length = int(len(line) / 2)
        segment_one = line[:segment_length]
        segment_two = line[segment_length:]

        matches = set()

        for char in segment_one:
            if char in segment_two:
                matches.add(get_char_value(char))

        total_sum += sum(matches)

    print(total_sum)
