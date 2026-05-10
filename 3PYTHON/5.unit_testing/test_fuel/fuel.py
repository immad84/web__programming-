def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))


def convert(fraction):
    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
        if y == 0:
            raise ZeroDivisionError('y is zero')
        if x > y:
            raise ValueError("x greator than y")
        div = x / y
        per = round(div * 100)
        return per
    except TypeError:
        pass
    except EOFError:
        print("EOF Error")
    except KeyboardInterrupt as e:
        print("Keyboard Interupt.")


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
