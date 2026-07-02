months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    date = input("Date: ").strip()

    try:

        if "/" in date:
            m, d, y = date.split("/")
            if 1 <= int(m) <= 12 and 1 <= int(d) <= 31:
                print(f"{int(y)}-{int(m):02}-{int(d):02}")
                break

        else:
            if "," in date:
                month_name, day_with_comma, y = date.split(" ")
                d = day_with_comma.replace(",", "")

                if month_name in months and 1 <= int(d) <= 31:
                    m = months.index(month_name) + 1
                    print(f"{int(y)}-{m:02}-{int(d):02}")
                    break
    except:
        pass
