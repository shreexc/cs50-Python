import inflect

p = inflect.engine()
ad_list = []

while True:
    try:
        ad = str(input("Name: "))
        ad_list.append(ad)
    except EOFError:
        print()
        break
output = p.join(ad_list)
print("Adieu, adieu, to", output)
