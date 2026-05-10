def main():
    dollars = dollars_to_float(input('How much was the meal ? '))
    percent = percent_to_float(input('What percentage would you like to tip ? '))
    print(f'Cost {dollars}, tip {percent}')
    tip = dollars * percent
    print(f'Leave ${tip:.2f}')

def dollars_to_float(d):
    d = d.replace('$', ' ').strip()
    return float(d)

def percent_to_float(p):
    p = p.replace('%', ' ').strip()
    return int(p) / 100

main()