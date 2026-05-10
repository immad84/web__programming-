def main():
    message = input("Input: ")
    # new_message = ''
    # for char in message:
    #     if not is_vowel(char): # if not vowel
    #         new_message += char
    # for char in message:
    #     if shorten(char):
    #         message = message.replace(char, '')

    print(f"Output: {shorten(message)}")


def shorten(word):

    for char in word:
        if char in "AaEeIiOoUu":  # in operatr return True or False
            word = word.replace(char, "")
    return word


if __name__ == "__main__":
    main()
