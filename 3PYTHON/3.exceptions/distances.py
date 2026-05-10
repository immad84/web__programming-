distances = {
    'voyager 1': '163',
    'vogager 2': '126',
    'pioneer 10': '36 AU',
    'new horizons': '80',
    'pioneer 11': '44 AU'
}

def main():
    spacecraft = input('Enter Spacecraft ? ')
    try:
        au = int(distances[spacecraft])
        # au = int(distances.get(spacecraft, 'Unknown'))
    except KeyError:
        print(f'\'{spacecraft}\' does not exist in dict.')
        return 
    except ValueError:
        print(f'Can\'t convert \'{distances[spacecraft]}\' to integer.')
        return
    # else:
    #     print(f'{spacecraft} is {convert(au)} meters away from earth')
    print(f'{spacecraft} is {convert(au)} meters away from earth')

def convert(au):
    return au * 149597870700

if __name__ == '__main__':
    main()