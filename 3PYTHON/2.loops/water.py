import random

def main():
    moisture = sample()
    days = 1
    # print(f'day {days}: Moisture is {moisture}%')
    print('day {:>3d}: Moistrue is {:.2f} %'.format(days, moisture))
    while moisture > 20:
        moisture = sample()
        days += 1
        # print(f'day {days}: Moisture is {moisture} %')
        print('day {d:>3}: Moisture is {m} %'.format(d = days, m = moisture))
    print('{}'.format('Time To Water'))

def sample():
    m = random.randrange(0, 100)
    return m

if __name__ == '__main__':
    main()