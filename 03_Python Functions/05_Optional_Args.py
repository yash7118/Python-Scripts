"""
Sometimes the arguments may not be necessary
"""

fname = input("Enter First Name: ")
mname = input("Enter Middle Name(Optional): ")
lname = input("Enter Last Name: ")


"""
Optional Parameters are always added towards the end of the arguments in the function.
"""
def get_formatted_name(first_name, last_name, middle_name=' '):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return  full_name.title()


full_name = get_formatted_name(fname, lname, mname)
print("Full name: "+full_name)