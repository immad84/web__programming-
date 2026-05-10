def main():
    answer = input('what is the answer to the Great Question of Life, \
the Universe and Everything ? ').lower().strip()
    print(get_response(answer))
    print(get_response_match(answer))

def get_response(ans):
    if ans == '42' or ans == 'forty-two' or ans == 'forty two':
        return 'Yes'
    else:
        return 'No'

def get_response_match(ans):
    match ans:
        case '42' | 'forty-two' | 'forty two':
            return 'Yes'
        case _:
            return 'No'

main()