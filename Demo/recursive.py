def sum(n):

    if n==1: # base condition
        return 1
    
    else: # recursive call
        return n+ sum(n-1)
    
n=int(input("Enter a number:"))
print("Sum of numbers from 1 to ",n,"is:",sum(n))

# Factrol of number using recursion
def fact(n):
    if n==0: # base condition
        return 1
    
    else: # recursive call
        return n* fact(n-1)
print("Factrial of ",5,"is:",fact(5))    
