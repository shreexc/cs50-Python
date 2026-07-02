import validators

def main():
    print(email_checker(input("What's your email address? ")))

def email_checker(email):
    mail = validators.email(email)
    if mail:
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()
