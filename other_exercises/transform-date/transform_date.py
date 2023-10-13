def transform_date(date_input):
    parsed_digits = date_input.split("-")
    output = f"{parsed_digits[2]}-{parsed_digits[1]}-{parsed_digits[0]}"
    return output


def main():
    print(transform_date("2022-11-19"))


if __name__ == "__main__":
    main()
