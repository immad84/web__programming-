import re


def main():
    url = input('Enter URL: ')
    if match := re.search(r'^(?:https?://)?(?:www\.)?twitter\.com/([a-z0-9_\.]+)$', url, re.IGNORECASE): 
        print(f'UserName : {match.group(1)}')
    else:
        print(f'Invalid.')


if __name__ == "__main__":
    main()
