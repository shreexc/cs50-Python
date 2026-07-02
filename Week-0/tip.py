# tip calculator

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    return float(d.replace("$", ""))
    percentage = float(p.replace("%", ""))
    return percentage / 100


def percent_to_float(p):
    return float(p.replace("%", "")) / 100
    percentage = float(p.replace("%", ""))
    return percentage / 100



main()
