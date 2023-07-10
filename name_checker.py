from ValidationException import ValidationException


def validate_file(filename):
    numbers = "0123456789"

    with open(filename, "r") as in_stream:
        for line_number, line in enumerate(in_stream, start=1):
            if line_number == 1:
                continue  # Skip the header line

            firstname, lastname, username, posts, likes, gamerewards = line.strip().split(',')
            for char in firstname:
                if char in numbers:
                    try:
                        firstname = int(firstname)
                    except ValueError:
                        # If numbers in firstname, raise a ValidationException
                        raise ValidationException(f"Invalid first name: {firstname}")


def test():
    try:
        validate_file("users.txt")
    except ValidationException as ve:
        print(ve)


test()
