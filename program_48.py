# 48. Language Choice Using match-case

print("1. English")
print("2. Marathi")
print("3. Hindi")
choice = int(input("Choose language: "))
match choice:
    case 1:
        print("You selected English")
    case 2:
        print("You selected Marathi")
    case 3:
        print("You selected Hindi")
    case _:
        print("Invalid choice")
