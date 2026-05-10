def main():
    message = input('What\'s your message ? ')
    print(convert(message))

def convert(m):
    m = m.replace(':', ' ').strip().upper()
    return m

main()