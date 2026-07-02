import random
import sys

def main():
    level = get_level()
    number = random.randint(1, level)

    while True:
        try:
            guess = int(input("Guess: "))
            if guess < 1:
                continue
            if guess < number:
                print("Too small!")
            elif guess > number:
                print("Too large!")
            else:
                print("Just right!")
                sys.exit()
        except ValueError:
            continue

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                return level
        except ValueError:
            continue

if __name__ == "__main__":
    main()
