import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
        
    try:
        file_name = is_valid_file(sys.argv)
        with open(f"{file_name}") as file:
            print(get_line_count(file))
    except ValueError as e:
        sys.exit(e)
    except FileNotFoundError:
        sys.exit("File does not exist")


def is_valid_file(arg):
    name = arg[1]
    is_extension_exist = name.rfind(".")
    if is_extension_exist < 0 or not name.endswith('py'):
        raise ValueError("Not a Python file")
    return name


def get_line_count(file):
    count = 0
    for line in file:
        row = line.strip()
        if row.startswith('#') or not row:
            continue
        count += 1
    return count



if __name__ == "__main__":
    print(get_line_count('test.py'))
