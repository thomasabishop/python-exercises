import os
from helpers import getPuzzleInput
from solution_02_A import solution

puzzle_input_path = os.path.join(os.path.dirname(__file__), "data/test_input.txt")
puzzle_input = getPuzzleInput(puzzle_input_path)


def test_solution():
    assert solution(puzzle_input) == 8
