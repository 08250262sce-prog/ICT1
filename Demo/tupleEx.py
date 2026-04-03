my_tuple=('Hello',123456)
print(type(my_tuple))#Data type of my_tuple is tuple
print(my_tuple)
print(my_tuple[0])#Accessing first element of the tuple
print(my_tuple[1])#Accessing second element of the tuple
a,b=my_tuple#Unpacking the tuple
print(b) #Tuples are immutable, we cannot change the value of an element in a tuple
new_tup=tuple(a) #convert string 'hello' to a tuple of characters
print(new_tup)
concatented_tuple=my_tuple+new_tup #Concatenating two tuples
print(concatented_tuple)#Concatenated tuple of my_tuple and new_tup
print(concatented_tuple[2:6:2])#Slicing the tuple from index 2 to 5 with a step of 2
print(concatented_tuple[::-1])#Reversing the tuple
print(my_tuple) #This will raise an error as my_tuple has been deleted


n=concatented_tuple[2:7:4]#Slicing the tuple from index 2 to 6 with a step of 4
print(n[::-1])#Reversing the sliced tuple

print(concatented_tuple[6:1:-4])#Slicing the tuple from index 6 to the end
print(concatented_tuple[::-4])#Slicing the tuple from index 1 to 5 with a step of 4
