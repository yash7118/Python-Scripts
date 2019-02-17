print("Tile: Program for List demo")

# Empty List
list01 = []
print("Printing list 01: ",list01)

# Adding values to empty list.
list01.append("2")
list01.append("-90.78")
list01.append("any string")

# Printing list 01
print ("List 01 with values: ",list01)

# Accessing element of list.
print("Accesing element 0: ", list01[0])
print("Accesing element 1*2:" , list01[1*2])
print("Accesing element -1: ", list01[-1])

# A list with values initialized
list02 = [2,3,"abc"]
print("Printing list 02: ", list02)

# Merging list01 and list02
print("Adding list 1 to 2 ",list01 + list02)

# Appending list 01 and list02
list01.append(list02)
print ("Appendend list01 + list 02: ",list01)

# Replacing List in the memory.
list01 = ["-2", "87.09", "demo"+"b" , 7+9]
print("Printing List 01: ",list01)

# Modifying a specific index value in List.
list01[0] = "2"
print("Modifying a specific index value in list: list01[0] = \"2\" " , list01)

# Inserting a value in the list at index=k
print("Inserting a value in the list at index=k=2: list.insert(k, value) ", list01.insert(2,"second"))

# Deleting a value in the list01 @index=k
del list01[2]
print("Delete a value in the list01 @index=k=1: del list[k]", list01)

# Popping last element in the list. pop()
popped_element = list01.pop()
print("Pop(): Remove the last element form the list, but hold value in a variable: list.pop() ->Popping: ", popped_element)
print("List after pop() ",list01)

# Popping element at a specific index=k
popped_element = list01.pop(1)
print("Popping the value at specific index=k: list.pop(k): Popped elem: ", popped_element)
print("List after pop(k) ",list01)

# Removing element from the list using a value.
list01.remove("demob")
print("Removing from the list: list.remove('2')" , list01)

# Calling list() constructor
data = "mydata"
backup = list(data)
print("Printing data backup - Backup list generated from data: backup=list(data): ", backup)

# Understanding List Function.

# Soring a list permanently
perm_sort = backup
perm_sort.sort()
print("Permanent Alphabetical Sort : perm_sort.sort(): ", perm_sort)

# Sorting a list permanently in reverse order.
rev_perm_sort = backup
rev_perm_sort.sort(reverse=True)
print("Permanent Reverse Alphabetical Sort: rev_perm_sort.sort(reverse=True): ",rev_perm_sort)

# Temporary alphabetical sort
print("Temporary Alphabetical Sort : sorted(backup): ", sorted(backup))

# Temporary reverse alphabetical sort.
print("Temporary Reverse Alphabetical Sort: sorted(backup, reverse=True): ",sorted(backup, reverse=True))

# Reversing the List.
rev_list = backup
rev_list.reverse()
print("Printing a list in reverse order: list.reverse() ", rev_list)

# Length of the list.
print("Length of list: "+str(len(backup)))

# Looping the lists.
magicians = ["goga", "ajoba", "nector", "victor"]
print_id = 1
# Accessing single element of list again,
print(str(print_id)+". I like tricks of Magician ", magicians[2].title())

# Loop to access all the elements in the list
for magician in magicians:
    print_id = print_id+1
    print(str(print_id)+". Magician enrolled for competition: " + magician.title())

# Making Numerical Changes:
# Understanding Use of Range() Function:

for value in range(1,5):
    print(value)

# List of Numbers
numbers = list(range(1,6))
print(numbers)

# List of Even Numbers
evenNumbers = list(range(2,11,2))
print(evenNumbers)

# List of squares
squares = []
for sq in range(1,11):
    square= sq**2
    squares.append(square)
print(squares)

# Simple list stats.

print("Minimum value of square: " + str(min(squares)))
print("Maximum value of square: " + str(max(squares)))
print("Sum of squares: " + str(sum(squares)))

# List Comphrehensions:
# list = [list_Val for val in range(a,b,x)]

sqList = [sq**2 for sq in range(1, 11)]
print(sqList)
cbList = [cb**3 for cb in range(1, 11)]
print(cbList)

# Slicing 0 to 4, prints elements 1,2,3
print(sqList[1:4])

# Slicing till end
print(sqList[4:])

# Slicing form beginnig
print(sqList[:6])

# Slicing from back:
print(sqList[-3:])

# Copying the list from one to another:
sqListBkup = sqList[:]

sqListPtr = sqList
sqList.append(11**2)
sqListPtr.append(12**2)

print("sqListBkup: " , sqListBkup)
print("sqListPtr: ", sqListPtr)
# --END OF FILE--