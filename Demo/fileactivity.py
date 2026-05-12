file = open('Students.xlsx', 'w')
file.write("Name, ID\n")
file.write("Sunita, 678\n")
file.write("Karma, 112\n")
file.write("Pema, 123\n")
file.write("Kuenzang, 234\n")
file.write("Monisha, 155\n")
file.close()
file = open('Students.xlsx', 'r')
students = file.read()
print(students)
file.close()
searchN = input("Enter a name to search: ")
found = False
with open('Students.xlsx', 'r') as file:
    for student in file:
        if searchN.lower() in student.lower():
            print(student)
            found = True
            break
if not found:
    print("Name not found in the file.")
print()