# 29. Basic Blood Donation Criteria

age = int(input("Enter age: "))
weight = float(input("Enter weight in kg: "))
if 18 <= age <= 65 and weight >= 50:
    print("Meets basic age and weight criteria")
else:
    print("Does not meet basic criteria")
print("Final eligibility requires medical screening.")
