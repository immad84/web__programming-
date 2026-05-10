def main():
    names = ['Mario', 'Luigi', 'Daisy', 'Yoshi']
    for name in names:
        print(write_letters(name, 'Princess Peach'))


def write_letters(receiver, sender):
    return f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    Dear {receiver},

    You are cordially invited to a ball at 
    Peach's Castle this evening, 7:30 PM.

    Sincerely,
    {sender}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
"""

if __name__ == '__main__':
    main()