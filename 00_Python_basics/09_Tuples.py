# List are mutable. A more immutable form of list is called tuples.
# Similar to list they are in ()

tuple = ()

D2 = (200, 40)
D3 = (5, 3, 4)

print(D2)
print(D3[2])

# This will give an error since tuples' elements cannot be reassigned, as they are immutable.
# D2[1] = 90

# But, tuples as a variable can be reassigned.

D3 = D2
print(D3)