name = "default_Name"
item = "default_item"


def some_statement(name, item):
    print(name + " has a/an " + item)


# Calling default value:
some_statement(name, item)

# Positional Arguments
some_statement("Yash", "laptop")
some_statement("Item", "Person")
print("So - positions matter in positional arguments")


# Keyword Arguments
some_statement(name="yash", item="car")
print("This is use of keyword based arguments ")

# Equivalent Functions:
some_statement(name, item="laptop")
some_statement("yash", item="car")
print("So, we have equivalent functions where everything can be mixed!")
