# 20. Ticket Price by Age

age = int(input("Enter age: "))
if age < 0:
    print("Invalid age")
elif age < 5:
    print("Ticket is free")
elif age < 18:
    print("Ticket price: Rs. 50")
elif age < 60:
    print("Ticket price: Rs. 100")
else:
    print("Ticket price: Rs. 60")
