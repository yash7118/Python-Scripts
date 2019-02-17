"""
A function can return any kind of data structure or values.
"""

fname = input("Please enter the first_name: ")
lname = input("Please enter the last name: ")
age = input("Please enter age(optional) :")


def build_person(first_name, last_name, age=''):
    person = {'first':first_name.title(), 'last':last_name.title()}
    if age:
        person['age']= age

    return person

person = build_person(fname, lname, age=age)
print(person)