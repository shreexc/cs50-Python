enter = input("Expression: ").split(" ")
if enter[1] == "+":
    print(float(enter[0]) + float(enter[2]))
elif enter[1] == "-":
    print(float(enter[0]) - float(enter[2]))
elif enter[1] == "*":
    print(float(enter[0]) * float(enter[2]))
elif enter[1] == "/":
    print(float(enter[0]) / float(enter[2]))
