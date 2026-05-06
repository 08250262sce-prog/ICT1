greetings=open("hello.txt","r")
print(greetings)

greetings.close()
 
f=open("hello.txt","r")
print("filename:",f.name)
print("file mode:",f.mode)
print("Is file closed?:",f.closed)
f.close()
print("Is file closed?:",f.closed)

f=open("hello.txt","r")
contents=f.read()
print(contents)
f.close()

newfile=open("newFile.txt","w")
print(newfile)

newfile.write("This is a new file created by python.")
newfile.close()

FileOverwrite=open("newFile.txt","w")
FileOverwrite.write("The contents of the newFILE is now changed.")
FileOverwrite.close()

appendFile=open("hello.txt","a")
appendFile.write("\n\n Dont forget to smile today!")
appendFile.close()

with open ("hello.txt","r") as f:
    contents=f.read()
    print(contents)