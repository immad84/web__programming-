import emoji

def main():
    emoji_string = input('Input: ')
    print_emoji(emoji_string)

def print_emoji(e):
    print(emoji.emojize(f'Output: {e}', language='alias'))

if __name__ == '__main__':
    main()

