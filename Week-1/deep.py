# 42 Forty Two forty-two

text = input("What is the answer to the great question of life, the universe, and everything? ").strip()
text = text.lower()
if text == "42" or text == "forty-two" or text == "forty two":
    print("Yes")
else:
    print("No")
