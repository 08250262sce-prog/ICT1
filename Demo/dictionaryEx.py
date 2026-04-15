userDetails={'Id':1,'userName':'Just_me'}
print(type(userDetails))#Data type of userDetails is dictionary
print(userDetails) #Printing the dictionary

locaction=dict(s='Samtse',t='Thimphu',p='Paro') #Creating a dictionary using dict() function as location with keys s,t,p and values Samtse, Thimphu and Paro respectively   
print(locaction) #Printing the dictionary created using dict() function as keys s,t,p and values Samtse, Thimphu and Paro respectively

print(userDetails['userName']) #Accessing the value of the key 'userName' in the userDetails dictionary
print(locaction.get('t')) #Accessing the value of the key 't' in the location dictionary using get() method

userDetails['email']='just_me@example.com' #Adding a new key-value pair to the userDetails dictionary
print(userDetails) #Printing the updated dictionary
userDetails['userName']='Just_me_updated' #Updating the value of the key 'userName' in the userDetails dictionary
print(userDetails) #Printing the updated dictionary

del locaction['p'] #Deleting the key-value pair with key 'p' from the location dictionary
print(locaction) #Printing the updated location dictionary after deletion of key 'p'

deleted_value=userDetails.pop('email') #Removing the key 'email' from the userDetails dictionary and storing its value in deleted_value
print(deleted_value) #Printing the value of the deleted key 'email'

del_key,del_value=userDetails.popitem() #Removing the last key-value pair from the userDetails dictionary and storing the key in del_key and value in del_value
print(f'the deleted key is {del_key} and the deleted value is {del_value}') #Printing the deleted key and value
locaction.clear() #Removing all key-value pairs from the location dictionary
print(locaction) #Printing the empty location dictionary after clearing all key-value pairs
