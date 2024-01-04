import os

puzzle_input_path = os.path.join(os.path.dirname(__file__), "data/input.txt")

with open(puzzle_input_path, "r") as f:
    total = 0
    lines = [line.strip() for line in f.readlines()]

    for line in lines:
        colour_sets = {"red": [], "green": [], "blue": []}
        colon_separator = line.index(":")
        games = line[colon_separator + 1 :].split(";")
        games = [item.strip().split() for game in games for item in game.split(",")]

        for counter_values in games:
            colour = counter_values[1]
            count = int(counter_values[0])
            colour_sets[colour].append(count)
        reduced = [max(colour_sets[colour]) for colour in colour_sets]
        reduced_product = 1

        for val in reduced:
            reduced_product *= val

        total += reduced_product
    print(total)
