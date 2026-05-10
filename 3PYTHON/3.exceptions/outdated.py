def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    date = input('Date: ')
    print(convert_date_format(date, months))

def convert_date_format(date, months):
    while True:
        try:
            if '/' in date:
                month, day, year = date.split('/')
                month = int(month)
                day = int(day)
                year = int(year)
                if 1 <= month <= 12 and 1 <= day <= 31:
                    return f'{year}-{month:02}-{day:02}'
            else:
                d, year = date.split(',')
                month, day = d.split()
                if month in months:
                    month = months.index(month) + 1
                    day = int(day)
                    if 1 <= month <= 12 and 1 <= day <= 31:
                        return f'{year.strip()}-{month:02}-{day:02}'
        except ValueError:
            pass

if __name__ == '__main__':
    main()
