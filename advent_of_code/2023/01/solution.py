import os

puzzle_input_path = os.path.join(os.path.dirname(__file__), "data/test_input.txt")


def getPuzzleInput(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file]


puzzle_input = getPuzzleInput(puzzle_input_path)


def solution(puzzle_input):
    print(puzzle_input)


solution(puzzle_input)
