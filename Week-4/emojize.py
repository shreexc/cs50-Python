import emoji

ask = str(input("Input: "))
give = emoji.emojize(ask, language="alias")
print("Output:", give)
