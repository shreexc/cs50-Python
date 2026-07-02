text = input('camelCase: ')
snake = ""

for char in text:
    if char.isupper():
        snake += '_' + char.lower()

    else: snake += char
print(f'snake_case: {snake}')
