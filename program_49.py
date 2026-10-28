# 49. Result Status Using match-case

status = input("Enter result status (pass/fail/absent): ").lower()
match status:
    case "pass":
        print("Congratulations! You passed.")
    case "fail":
        print("Better luck next time.")
    case "absent":
        print("You were absent.")
    case _:
        print("Invalid status")
