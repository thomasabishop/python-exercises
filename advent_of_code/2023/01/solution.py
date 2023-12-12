import os

puzzle_input_path = os.path.join(
    os.path.dirname(__file__), "data/test_input.txt")


def getPuzzleInput(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file]


puzzle_input = getPuzzleInput(puzzle_input_path)


def solution(puzzle_input):
    count = 0
    for item in puzzle_input:
        characters = list(item)
        integers = [i for i in characters if i.isnumeric()]
        count += int(integers[0] + integers[-1])
    return count


print(solution(puzzle_input))
