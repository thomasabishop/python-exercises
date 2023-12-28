import os
from helpers import getPuzzleInput

puzzle_input_path = os.path.join(os.path.dirname(__file__), "data/input.txt")
puzzle_input = getPuzzleInput(puzzle_input_path)


def solution(puzzle_input):
    initial_values = {"red": 12, "green": 13, "blue": 14}
    valid_games_count = 0
    for line in puzzle_input:
        colon_separator = line.index(":")
        game_number = int(line[:colon_separator].split()[1])
        games = line[colon_separator + 1 :].split(";")
        games = [item.strip().split() for game in games for item in game.split(",")]
        for counter_values in games:
            colour = counter_values[1]
            count = int(counter_values[0])
            if colour in initial_values.keys() and count > initial_values[colour]:
                break
        else:
            valid_games_count += game_number
    return valid_games_count


print(solution(puzzle_input))
