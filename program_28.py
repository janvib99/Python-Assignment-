# 28. Shopping Discount

amount = float(input("Enter shopping amount: "))
if amount < 0:
    print("Invalid amount")
else:
    if amount >= 5000:
        discount = amount * 0.20
    elif amount >= 2000:
        discount = amount * 0.10
    else:
        discount = 0
    print("Discount:", discount)
    print("Final amount:", amount - discount)
