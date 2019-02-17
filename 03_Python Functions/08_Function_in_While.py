"""
Optional Parameters are always added towards the end of the arguments in the function.
"""


def get_formatted_name(first_name, last_name, middle_name=' '):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return  full_name.title()


while True:
    print("Plese enter required details, press 'q' anytime to Quit.")
    fname = input("Enter First Name: ")
    mname = input("Enter Middle Name(Optional): ")
    lname = input("Enter Last Name: ")

    if fname == 'q' or mname == 'q' or lname == 'q':
        print("Thanks for information, See you later!")
        break

    full_name = get_formatted_name(fname, lname, mname)
    print("Full name: "+full_name)

