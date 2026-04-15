name=input("Enter your name: ")
for i in name:
    print(i)

li=["Python Programming","Python Fumdamentals","Python Intrivew Questions"]
for x in li:# x is the variable that takes the value of each element in the list during each iteration of the loop
    print(x)

lenli=len(li)#len()returns the no. of items in the list li i.e.3 This value is stored in the variable lenli
for x in range(lenli):
    print(li[x]) # x is a variable that takes the value of each index.

new_tuple=tuple(li)
for i in new_tuple:
    print(i)

new_set=set(li)
for i in new_set:
    print(i)




