from datetime import date
import sys

ONES = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
        "seventeen", "eighteen", "nineteen"]
TENS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
SCALES = ["", "thousand", "million", "billion", "trillion"]


def main():
    print(minutes(input("Date of Birth: ")))


def minutes(dob):
    try:
        year, month, day = (int(x) for x in dob.split("-"))
        birth_date = date(year, month, day)
    except (ValueError, TypeError):
        sys.exit("Invalid date")

    today = date.today()
    days_alive = (today - birth_date).days
    minutes_alive = days_alive * 24 * 60

    return f"{number_to_words(minutes_alive).capitalize()} minutes"


def three_digit_words(n):
    parts = []
    if n >= 100:
        parts.append(f"{ONES[n // 100]} hundred")
        n %= 100
    if n >= 20:
        word = TENS[n // 10]
        if n % 10:
            word += f"-{ONES[n % 10]}"
        parts.append(word)
    elif n > 0:
        parts.append(ONES[n])
    return " ".join(parts)


def number_to_words(n):
    if n == 0:
        return "zero"

    groups = []
    scale_index = 0
    while n > 0:
        n, remainder = divmod(n, 1000)
        if remainder:
            groups.append((remainder, scale_index))
        scale_index += 1

    words = []
    for value, scale in reversed(groups):
        part = three_digit_words(value)
        if SCALES[scale]:
            part += f" {SCALES[scale]}"
        words.append(part)

    return ", ".join(words)


if __name__ == "__main__":
    main()
