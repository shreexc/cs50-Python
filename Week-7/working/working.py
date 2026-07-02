import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"

    match = re.search(pattern, s.strip())
    if not match:
        raise ValueError("Invalid time format")

    sh, sm, sp, eh, em, ep = match.groups()

    start_hour = int(sh)
    end_hour   = int(eh)

    start_min = sm if sm else "00"
    end_min   = em if em else "00"

    if sp == "PM" and start_hour != 12:
        start_hour += 12
    elif sp == "AM" and start_hour == 12:
        start_hour = 0

    if ep == "PM" and end_hour != 12:
        end_hour += 12
    elif ep == "AM" and end_hour == 12:
        end_hour = 0

    if not (0 <= start_hour <= 23 and 0 <= end_hour <= 23):
        raise ValueError("Invalid hour")
    if not (0 <= int(start_min) <= 59 and 0 <= int(end_min) <= 59):
        raise ValueError("Invalid minute")

    return f"{start_hour:02}:{start_min} to {end_hour:02}:{end_min}"


if __name__ == "__main__":
    main()
