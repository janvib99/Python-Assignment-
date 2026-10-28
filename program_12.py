# 12. Child or Adult

age = int(input("Enter age: "))
if age < 0:
    print("Invalid age")
elif age < 18:
    print("Child")
else:
    print("Adult")
