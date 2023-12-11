import string
from pathlib import Path

test_input = Path(__file__).parent / "input_test.txt"


def parse_pairs(lines):
    tuple_pairs = []


def populate_pair_values(pair: tuple[int, int]) -> list[int]:
    return [i for i in range(pair[0], pair[1] + 1)]


# def is_full_overlap(pair_list_one, pair_list_two):
# use set operations to determine if there is a full overlap
# does the smallest list exist as a subset of the largest list?


def main():
    # range_one = (2, 3)
    range_two = (1, 4)

    # values = list(range(range_two[0], range_two[1] + 1))
    # values = extract_pair_values(range_two)
    # print(values)

    with test_input.open() as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        print(parse_pairs(lines))


if __name__ == "__main__":
    main()
