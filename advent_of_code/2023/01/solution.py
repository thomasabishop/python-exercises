import os

puzzle_input_path = os.path.join(
    os.path.dirname(__file__), "data/test_input.txt")


def getPuzzleInput(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file]


puzzle_input = getPuzzleInput(puzzle_input_path)


def solution_one(puzzle_input):
    count = 0
    for item in puzzle_input:
        integers = [i for i in list(item) if i.isnumeric()]
        count += int(integers[0] + integers[-1])
    return count


# print(solution_one(puzzle_input))
mock_input = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen"
]


def solution_two(puzzle_input):
    mapping = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    mapping_keys = list(mapping.keys())
    possible_words = []
    for line in puzzle_input:
        for char in line:
            running_word_chars = []
            running_word = ''.join(running_word_chars)
            if not char.isnumeric():
                running_word.append(char)
                if running_word in mapping_keys:
                    print(running_word)
                else:
                    continue

    solution_two(mock_input)
    #     matches = []
    #     for key in mapping_keys:
    #         if item.find(key) != -1:
    #             matches.append(key)
    #     all_matches.append(matches)
    # return all_matches


# def parse_line(line, array_to_match):
#     matches = []
#     reconstructed_substring = []
#     for char in line:
#         word = ''.join(reconstructed_substring)
#         if word in array_to_match:
#             matches.append(word)
#             continue
#         reconstructed_substring.append(char)
#         print(reconstructed_substring)
#         print(word)

#     return matches


# test_line = "shoesandfive"
# test_match_array = ["five", "table"]

# print(parse_line(test_line, test_match_array))


# solution_two(mock_input)
# print(solution_two(mock_input))
