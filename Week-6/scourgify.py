import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

before = sys.argv[1]
after = sys.argv[2]

if not before.endswith(".csv") or not after.endswith(".csv"):
    sys.exit("Not a CSV file")

students = []

try:
    with open(before) as file:
        reader = csv.DictReader(file)
        for row in reader:
            last, first = row["name"].split(", ")
            students.append({"first": first, "last": last, "house": row["house"]})
except FileNotFoundError:
    sys.exit(f"Could not read {before}")
except KeyError:
    sys.exit("Invalid CSV format")

try:
    with open(after, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        writer.writerows(students)
except:
    sys.exit("Could not write output file")
