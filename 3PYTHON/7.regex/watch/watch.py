import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r"<iframe src=\"(?P<http>https?://)?(?:www\.)?(?P<embed>youtube\.com/embed/[a-z0-9_\.]+)\"></iframe>"
    # pattern = r'(?P<http>https?://)?(?:www\.)?(?P<embed>youtube\.com/embed/[a-z0-9_\.]+)'
    match = re.search(pattern, s, re.IGNORECASE)
    if match:
        http = match.group("http") if match.group("http") == "https://" else "https://"
        embed = match.group("embed")
        embed = embed.replace("youtube.com/embed", "youtu.be")
        return http + embed
    else:
        return None


if __name__ == "__main__":
    main()
