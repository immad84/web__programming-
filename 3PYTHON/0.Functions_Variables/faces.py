def main():
    # get the user input
    message = input('What\'s your message ? ')
    # call the convert fun to change input
    print(convert(message))

def convert(text):
    text = text.replace(':)', '🙂')
    text = text.replace(':(', '🙁')
    return text

main()