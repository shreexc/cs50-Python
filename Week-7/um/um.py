import re
import sys


def main():
    print(count(input("Text: ")))

def count(s):
    word_count = re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(word_count)

if __name__ == "__main__":
    main()
