from solution import solution_one, solution_two


def test_solution_one():
    mock_input = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
    assert solution_one(mock_input) == 142


def test_solution_two():
    mock_input = [
        "two1nine",
        "eightwothree"
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen"
    ]
    assert solution_two(mock_input) == 281
