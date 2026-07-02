import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if not re.search(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip):
        return "False"

    octets = ip.split(".")

    for octet in octets:
        if not (0 <= int(octet) <= 255):
            return "False"

    return "True"


if __name__ == "__main__":
    main()
