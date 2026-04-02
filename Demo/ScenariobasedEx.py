student_name=input("Enter student  name:")
days_borrowed=int(input("Number of days book  was borrowed:"))
days_late=int(input("0 if returned on time:"))
fine_per_day=0
total_fine=0
warning_message=""
if days_late==0:
    fine_per_day=0
elif 1<=days_late <=5:
     fine_per_day=5 
elif 6<=days_late <=10:   
   fine_per_days=10
else:
    fine_per_day=20
total_fine=fine_per_day*days_late
if days_borrowed <30:
    display_warnning=("Librsry privilage may be restricted:")
print("Student name:",student_name)
print("Days borrowed:",days_borrowed) 
print("Days late:",days_late)
print("Fine per day:",fine_per_day)
print("Total fine:",total_fine)



  




