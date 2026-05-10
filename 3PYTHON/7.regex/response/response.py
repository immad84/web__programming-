from validator_collection import validators, errors


def main():
    print(is_valid(input("What's your email address? ")))


def is_valid(email):
    try:
        validators.email(email)
        return "Valid"
    except errors.EmptyValueError:
        return "Invalid"
    except errors.InvalidEmailError:
        return "Invalid"


if __name__ == "__main__":
    main()
