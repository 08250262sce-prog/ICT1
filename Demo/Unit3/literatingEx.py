tup=("John Smith","Jane Doe","Alice Johnson")
for x in tup:
    print(x)

set1={10,30,20}
for x in set1:
    print(x)

Bookdetails=dict({"Python Programming":"John Smith","Python Fumdamentals":"Alice Johnson","Python Intrivew Questions":"Jane Doe"})
for keys in Bookdetails:#keys is a variable that takes the value of each key in the dictionary
    print(keys,Bookdetails[keys])
