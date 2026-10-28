# 31. Positive and Even Using Nested If

n = int(input("Enter a number: "))
if n > 0:
    if n % 2 == 0:
        print("Positive and even")
    else:
        print("Positive but odd")
else:
    print("Number is not positive")
