print()#printing empty line for better readability
student_list=[]#craeting an empty list to store student names
student_age=set()#creating an empty set to store student ages
student_grade=set()#creating an empty set to store student grades
student_dict={}#creating an empty dictionary to store student names as keys and their ages and grades as values

student_list.append("Arjun Bhattarai")#adding student names to the list
student_list.append("Sita Sharma")#adding student names to the list
student_list.append("Ram Thapa")#adding student names to the list
student_list.append("Tika Maya")#adding student names to the list

student_age.add(20)#adding student ages to the set
student_age.add(22)#adding student ages to the set  
student_age.add(21)#adding student ages to the set
student_age.add(23)#adding student ages to the set

student_grade.add("A")#adding student grades to the set
student_grade.add("B")#adding student grades to the set 
student_grade.add("D")#adding student grades to the set 
student_grade.add("C")#adding student grades to the set

student_dict["Arjun Bhattarai"]={"age":20,"grade":"A"}#adding student name as key and their age and grade as value in the dictionary
student_dict["Sita Sharma"]={"age":22,"grade":"B"}#adding student name as key and their age and grade as value in the dictionary  
student_dict["Ram Thapa"]={"age":21,"grade":"D"}#adding student name as key and their age and grade as value in the dictionary
student_dict["Tika Maya"]={"age":23,"grade":"C"}#adding student name as key and their age and grade as value in the dictionary

add_student=input("Enter the name of the student to add or else enter to skip: ")#taking input from user to add a new student name
add_age=int(input("Enter the age of the student: "))#taking input from user to add a new student age
add_grade=input("Enter the grade of the student: ")#taking input from user to add a new student grade
if add_student:#checking if the user has entered a student name
    student_list.append(add_student)#adding the new student name to the list
    student_age.add(add_age)#adding the new student age to the set
    student_grade.add(add_grade)#adding the new student grade to the set
    student_dict[add_student]={"age":add_age,"grade":add_grade}#adding the new student name as key and their age and grade as value in the dictionary
    print(f"student added successfully! The age of the student'{add_student} is {student_dict}[add_student]['age'] and the grade is {student_dict[add_student]['grade']}") #printing the details of the newly added student
else:
     print("No student added.")#printing message if no student is added
print()#printing empty line for better readability
search_name=input("Enter the name of the student to search: ")#taking input from user to search for a student name
if search_name in student_list:#checking if the searched student name is in the list
    print(f"student found! The age of the student'{search_name}' is {student_dict[search_name]['age']} and the grade is {student_dict[search_name]['grade']}")#printing the details of the searched student
else:
    print("student not found.")#printing message if the searched student name is not found in the list

    print()#printing empty line for better readability
remove_student=input("Enter the name of the student to remove or else enter to skip: ")#taking input from user to remove a student name
if remove_student:#checking if the user has entered a student name to remove
    if remove_student in student_list:#checking if the student name to remove is in the list
        remove_age=student_dict[remove_student]["age"]#getting the age of the student to remove from the dictionary
        remove_grade=student_dict[remove_student]["grade"]#getting the grade of the student to remove from the dictionary
        student_list.remove(remove_student)#removing the student name from the list

        del student_dict[remove_student]#removing the student name and its details from the dictionary
        print("student removed successfully!")#printing message if the student is removed successfully
        print("student left along with their details:", student_dict)#printing the remaining students and their details in the dictionary
        print("List of students left:", student_list)#printing the remaining student names in the list
    else:        
        print("student not found ")#printing message if the student name to remove is not found in the list
print()#printing empty line for better readability