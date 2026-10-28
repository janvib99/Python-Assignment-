# 24. Exam Result

marks = int(input("Enter marks (0-100): "))
if not 0 <= marks <= 100:
    print("Invalid marks")
elif marks >= 75:
    print("Distinction")
elif marks >= 60:
    print("First Class")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")
