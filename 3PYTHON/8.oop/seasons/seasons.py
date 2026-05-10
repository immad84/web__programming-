from datetime import date
import sys
import inflect


def main():
    try:
        dob = date.fromisoformat(input("Date of Birth: "))
        today = date.today()
        print(get_age_words(dob, today))
    except ValueError:
        sys.exit("Invalid date")


def get_age_words(dob, today):
    p = inflect.engine()
    age_minutes = get_age_minutes(dob, today)
    words = p.number_to_words(round(age_minutes), andword="") + " minutes"
    return words.capitalize()


def get_age_minutes(dob, today):
    extra_minutes = 0
    for year in range(dob.year, today.year + 1):
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            extra_minutes += 1440
    return (today - dob).days * 24 * 60


if __name__ == "__main__":
    main()
