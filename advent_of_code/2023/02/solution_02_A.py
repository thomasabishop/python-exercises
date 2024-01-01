import os

puzzle_input_path = os.path.join(os.path.dirname(__file__), "data/test_input.txt")

with open(puzzle_input_path, "r") as f:
    initial_values = {"red": 12, "green": 13, "blue": 14}
    valid_games_count = 0
    lines = [line.strip() for line in f.readlines()]

    for line in lines:
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
print(valid_games_count)
