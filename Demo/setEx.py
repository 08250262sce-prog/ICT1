my_set={1,2,3,"Hello",3.14,1,2,False} #Creating a set with duplicate values 
print(type(my_set))#Data type of my_set is set
print(my_set) #Sets do not allow duplicate values, so the duplicate values will be removed
#my_set[0]="Start" #This will raise an error as sets are unordered and do not support indexing aditionally, set are immutable
my_set.add("World") #Adding an element to the set
print(my_set) #Set after adding an element
my_second_set={3,4,5} #Creating another set
union_set=my_set.union(my_second_set) #Union of two sets
print(union_set) #Union of my_set and my_second_set only unique elements will be included and if there is double element then one will be exicuted
intersection_set=my_set.intersection(my_second_set) #Intersection of two sets
print(intersection_set) #Intersection of my_set and my_second_set only common elements will be  
difference_set=my_set.difference(my_second_set) #Difference of two sets
print(difference_set)# printing different set which are not there or execuited
my_set.clear() #Clearing the set
print(my_set) #Set after clearing all elements