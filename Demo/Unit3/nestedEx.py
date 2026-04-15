for i in range(1,4):# outer loop iterates from 1 to 3
    for j in range(i):# inner loop iterates from 0 to i-1
        print(f"outer loop iteration{i},inner loop iteration{j+i}")

for i in range (4):# it represents the no. of rows of stars to printed. It iterate from 0 to 3, which means it will print 4 rows of stars
    for j in range(i):#it represent the no. of stars to be printed in each row
        print("*", end ="")#end paramater is used to specify what to print at the end of the output. By default, it is a newline character but  herevwe rae using same space to print the stars in gthe same line.
    print()# print a newline character after each row of stars

#Student Activity
for i in range(1,6):
    for j in range(1,1+i):
         print(j,end="")
    print() 

for i in range(6,0,-1):
    for j in range(i):
        print("*", end= " ")
    print()

