while True:
    ask = input("Fraction: ")

    try:
        numerator, denominator = ask.split("/")
        n = int(numerator)
        d = int(denominator)

        if n > d:
            continue

        percentage = round((n / d) * 100)
        break

    except (ValueError, ZeroDivisionError):
        pass

if percentage <= 1:
    print("E")
elif percentage >= 99:
    print("F")
else:
    print(f"{percentage}%")
