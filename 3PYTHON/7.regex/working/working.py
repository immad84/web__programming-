import re
import sys


def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError as e:
        sys.exit("ValueError")


def convert(s):
    pattern = r"^((?P<start>0?([0-9]|1[0-2]):?([0-5][0-9])? (AM|PM)) *((to)?) *(?P<end>0?([0-9]|1[0-2]):?([0-5][0-9])? (AM|PM)))$"
    match = re.search(pattern, s)
    if not match:
        raise ValueError
    start_time = match.group("start").lower().strip()
    end_time = match.group("end").lower().strip()
    return str(change_format(start_time)) + " to " + str(change_format(end_time))


def change_format(time):
    if time.endswith("am"):
        time = time.replace("am", " ").strip()
        hour, minute = time.split(":") if ":" in time else (time, "00")
        hour = int(hour)
        minute = int(minute)
        if hour == 12:
            hour = 0
    elif time.endswith("pm"):
        time = time.replace("pm", " ").strip()
        hour, minute = time.split(":") if ":" in time else (time, "00")
        hour = int(hour)
        minute = int(minute)
        if hour != 12:
            hour += 12
    hour = "0" + str(hour) if hour in range(0, 10) else str(hour)
    minute = "0" + str(minute) if minute in range(0, 10) else str(minute)
    return hour + ":" + minute


if __name__ == "__main__":
    main()
