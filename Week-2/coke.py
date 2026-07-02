amount_due = 50

while amount_due > 0:
    print(f"Amount Due: {amount_due}")
    coin = int(input("Insert Coin: "))

    if coin in [25, 10, 5]:
        amount_due -= coin

change_owed = abs(amount_due) if amount_due < 0 else 0
print(f"Change Owed: {change_owed}")
