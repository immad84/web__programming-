def main():
    message = input('Input: ')
    # new_message = ''
    # for char in message:
    #     if not is_vowel(char): # if not vowel
    #         new_message += char
    for char in message:
        if is_vowel(char):
            message = message.replace(char, '')
    print(f'Output: {message}')


def is_vowel(c):
    return c in 'AaEeIiOoUu' # in operatr return True or False

if __name__ == '__main__':
    main()

