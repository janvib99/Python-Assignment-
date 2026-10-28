# 22. Salary Bonus by Years of Service

salary = float(input("Enter salary: "))
years = int(input("Enter years of service: "))
if salary < 0 or years < 0:
    print("Invalid input")
elif years >= 5:
    bonus = salary * 0.10
    print("Bonus:", bonus)
else:
    print("No bonus")
