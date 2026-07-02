enter = input("Input: ")

for vowel in enter:
    if vowel.lower() not in ["a", "e", "i", "o", "u"]:
        print(vowel, end="")
