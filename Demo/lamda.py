name= input("Enter your name")
greet=lambda x: print ("Hello",x)
greet(name)

even_odd= lambda x: "Even" if x%2==0 else "Odd"
num=int(input("Enter a number:"))
print(even_odd(num))

arith= lambda x,y: (x+y,x-y,x*y,x/y)
num1=int(input("Enter first numer:"))
num2=int(input("Enter second number:"))
print(arith(num1,num2))

mylist=[1,2,3,4,5,6]
even=filter(lambda x:x%2==0, mylist)
print(list(even))

mylist=[1,2,3,4]
double=map(lambda x: x*2,mylist)
# print(list(double))

mynewlist=(list(double))
print(mynewlist)
division=map(lambda x:x/2,mynewlist)
print(list(division))

from functools import reduce
mylist=[1,2,3,4]
mul=reduce(lambda x,y: x*y,mylist)
print(mul)


#student activty
number=lambda x:"positive" if x>0 else "zero" if x==0 else "negative"
user_input=int(input("Enter the number:"))
print(number(user_input))

