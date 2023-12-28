import os
from helpers import getPuzzleInput

puzzle_input_path = os.path.join(os.path.dirname(__file__), "data/test_input.txt")
puzzle_input = getPuzzleInput(puzzle_input_path)


def solution(puzzle_input):
    count = 0
    for item in puzzle_input:
        integers = [i for i in list(item) if i.isnumeric()]
        count += int(integers[0] + integers[-1])
    return count


print(solution(puzzle_input))
