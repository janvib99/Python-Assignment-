# 40. Valid Password Using Nested If

password = input("Enter password: ")
if len(password) >= 8:
    if any(ch.isdigit() for ch in password):
        print("Valid password")
    else:
        print("Password must contain a digit")
else:
    print("Password must have at least 8 characters")
