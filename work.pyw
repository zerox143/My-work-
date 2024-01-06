# 3-1. Names: Store the name of few of your friends in a list called names. Print
# each person's name by accessing each element in the list one at a time.
names = ['ali' , 'ahmed' , 'asif' , 'hadi']
#             1            2         3          4
# print(bicycle)
print(names[0])
# applying title method to first element of array 
# print (bicycles[0].title())
# now we will acess element at pposition 2 and 4
print(names[1])
# print (bicycle[3])
# now we will use negative indexing
print(names[-1])
# using formatted string to display custom message
message = f"My first friend was a {names[0].title()}"
print(message)
message = f"My second friend was a {names[1].title()}"
print(message)
message = f"My third friend was a {names[2].title()}"
print(message)
message = f"My forth friend was a {names[3].title()}"
print(message)
# message = f"My first bicycle was a {names[4].title()}"
#print(message)
# accessing all elements of list at once
message = f"My First frined was a {names[0].title()}", f"My Second frined was a {names[1].title()}", f"My Third frined was a {names[2].title()}"
print(message)