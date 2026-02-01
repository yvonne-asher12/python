#prompting the user to enter names
names = []
name = (input("Enter your list:"))
while name != "":
    names.append(name)
    name = input("Enter your list:")
#sorting the list
names.sort()

#removing duplicates
names = list(set(names))

#displaying the final sorted list
print (names)

#counting and printing the total no of names
print(len(names))

