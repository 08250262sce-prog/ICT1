Name = str(input("Enter your name: "))
M1 = float(input("Enter marks for module 1: "))
M2 = float(input("Enter marks for module 2: "))
M3 = float(input("Enter marks for module 3: "))
M4 = float(input("Enter the marks for module 4:"))
Attendance = float(input("Enter attendance percentage: "))
Avg = (M1 + M2 + M3 + M4) / 4
print("Student Name: ", Name)
print(f"Average Marks: {Avg:.2f}")
print(f"Attendance: {Attendance:.2f}%")
if Avg >= 40 and Attendance >= 80:
    print("Result: Pass")
else:
    print("Result: Fail")
#checking Grade
if Avg >=90 and Attendance >=80:
    print("Grade: A")
elif Avg >=70 and Attendance >=80:
    print("Grade: B")
elif Avg >=60 and Attendance >=80:
    print("Grade: C")
elif Avg >=40 and Attendance >=80:
    print("Grade: D")
else:
    print("Grade: F")

#checking eligibility for reward
if Avg >= 90 or (Avg >=85 and Attendance >= 80):
    print("Eligible for reward: Yes")
else:
    print("Eligible for reward: No")