"""
A function cannot always display the output directly.
Instead it can process some data and return the value of the processed data
"""

fname = input("Enter First Name: ")
lname = input("Enter Last Name: ")

def get_formatted_name(first_name, last_name):
    full_name = first_name+ ' ' + last_name
    return  full_name.title()

full_name = get_formatted_name(fname, lname)
print("Full name: "+full_name)