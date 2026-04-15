no_of_student=int(input("Enter the number of students: "))#taking input from user to add multiple student names
i=1#initializing a variable i to 1 to keep track of the number of students added
student_names={}#creating an empty dictionary to store student names 
while i<=no_of_student:#using while loop to add student names until the number of students added is less than or equal to the number of students specified by the user
    name=input("Enter the name of student: ")#taking input from user to add a student name
    print("The name of the student{} is {}".format(i,name))#printing the name of the student added
    i+=1#incrementing the variable i by 1 to keep track of the number of students added
    student_names[i]=name#adding the student name to the dictionary with the key as the number of students added

print(student_names)# it prints the dictionary student_names which contains the student names added by the user with their corresponding keys as the number of students added   

while True:
    print("This is an infinite loop. Press Ctrl+C to stop it.")#printing a message to indicate that this is an infinite loop

 # control loop
for i in range (4):
    if i == 2:
        break# it breaks the loop when i is equal to 2
    print(i)
print("Loop ended")# it prints a message after the loop is ended    
