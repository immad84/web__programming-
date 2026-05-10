import re

def main():
    code = input('Hexadecimal Code: ')
    if match := re.search('^(?P<hex_code>#[a-fA-F0-9]{6})$', code, flags=re.IGNORECASE):
        print(f'Valid Match, {match.group("hex_code")}') # return the whole matched string.
    else:
        print(f'Invalid Match')

if __name__ == '__main__':
    main()