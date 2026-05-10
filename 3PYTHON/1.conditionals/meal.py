def main():
    time = input('What time is it ? ')
    get_meal_time(convert(time))

def convert(t):
    if t.endswith('a.m') or t.endswith('p.m'):
        t = t.replace('a.m', 'am')
        t = t.replace('p.m', 'pm')
        return convert_12_to_24_format(t)
    else:
        hour, minute = t.split(':')
        hour = int(hour)
        minute = int(minute)
        return round(hour + minute * (1 / 60), 2)

def convert_12_to_24_format(t_12):
    if t_12.endswith('am'):
        hour, minute = t_12.replace('am', ' ').strip().split(':')
        hour = int(hour)
        minute = int(minute)
        if hour == 12:
            hour = 0
    elif t_12.endswith('pm'):
        hour, minute = t_12.replace('pm', ' ').strip().split(':')
        hour = int(hour)
        minute = int(minute)
        if hour != 12:
            hour += 12
    return round(hour + minute * (1 / 60), 2)
        
def get_meal_time(d_time):
    if 7 <= d_time <= 8:
        print('breakfast time')
    elif 12 <= d_time <= 13:
        print('lunch time')
    elif 18 <= d_time <= 19:
        print('dinner time')

if __name__ == '__main__':
    main()
