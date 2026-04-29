def fun1(x,y):

    if x==0: # base condition
        return y
    
    else: # recursive call
        return fun1(x-1,y+x)
    
x=int(input("Enter the number of x:"))
y=int(input("Enter the number of y:"))
print("The result is:",fun1(x,y))
print("The result is:",fun1(x-1,y+x))

    
    