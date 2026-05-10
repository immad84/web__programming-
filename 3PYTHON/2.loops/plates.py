def main():
    plate = input('Plate: ')
    if is_valid(plate):
        print('Valid')
    else:
        print('Invalid')

def is_valid(plate):
    # check length of letters on plate
    if not 2 <= len(plate) <= 6:
        return False
    
    # check first two letters
    first_letters = plate[0:2]
    if not first_letters.isalpha():
        return False
    
    # check periods and punctuations
    if not plate.isalnum():
        return False
    
    # check last letters on plate
    last_letters = plate[2:]
    if last_letters.isalnum():
        for i in range(len(last_letters)):
            if last_letters[i].isdigit():
                # if last_letters[i] == '0':
                #     return False
                # if not last_letters[i:].isdigit():
                #     return False
                # break
                if last_letters[i] != '0' and last_letters[i:].isdigit():
                    return True
                else:
                    return False
    return True

# def is_valid(plate):
    # # check lenght of plate
    # if 2 <= len(plate) <= 6:
    #     # check first two letters
    #     first_letters = plate[0:2]
    #     if first_letters.isalpha():
    #         # check last four letters
    #         last_letters = plate[2:]
    #         if last_letters.isalpha():
    #             return True
    #         elif last_letters.isnumeric():
    #             if not last_letters.startswith('0'):
    #                 return True
    #         elif last_letters.isalnum():
    #             for i in range(len(last_letters)):
    #                 if last_letters[i].isdigit():
    #                     if last_letters[i:].isdigit():
    #                         if not last_letters[i].startswith('0'):
    #                             return True
    #                     break
    # return False


if __name__ == '__main__':
    main()
