# 14. Uppercase or Lowercase

ch = input("Enter a character: ")
if len(ch) == 1 and ch.isupper():
    print("Uppercase")
elif len(ch) == 1 and ch.islower():
    print("Lowercase")
else:
    print("Not an uppercase or lowercase letter")
