"""
A function can return any kind of data structure or values.
"""

fname = input("Please enter the first_name: ")
lname = input("Please enter the last name: ")


def build_person(first_name, last_name):
    person = {'first':first_name.title(), 'last':last_name.title()}
    return person


person = build_person(fname, lname)
print(person)