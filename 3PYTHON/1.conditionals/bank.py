def main():
    greeting = input('Greeting: ').lower().strip()
    print(get_penality(greeting))
    print(get_penality_match(greeting))

def get_penality(s):
    if s.startswith('hello'):
        return '$0'
    elif s.startswith('h'):
        return '$20'
    else:
        return '$100'

def get_penality_match(s):
    is_hello = True if s.startswith('hello') or s.startswith('h') else False
    match is_hello:
        case True:
            if s.startswith('hello'):
                return '$0'
            else:
                return '$20'
        case False:
            return '$100'
        
if __name__ == '__main__':
    main()

# class Welcomer:
#     def __init__(self):
#         self.greeting_message = ''

#     def welcome_message(self):
#         self.greeting_message = input('Greeting: ')

#     def get_penality(self):
#         s = self.greeting_message.lower().strip()
#         if s.startswith('hello'):
#             print('$0')
#         elif s.startswith('h'):
#             print('$20')
#         else:
#             print('$100')
    

