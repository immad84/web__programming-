distances = {
    'voyager 1': 163,
    'vogager 2': 126,
    'pioneer 10': 36,
    'new horizons': 80,
    'pioneer 11': 44
}

def main():
    for distance in distances.values():
        print(f'{distance} AU is {convert(distance)} meters')

def convert(distance):
    return distance * 149597870700

if __name__ == '__main__':
    main()