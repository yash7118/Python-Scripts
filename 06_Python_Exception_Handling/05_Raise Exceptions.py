"""
Sometimes, it may be important to raise exceptions.

raise keyword is  used to raise the exceptions.
"""

# raise NameError("a. Name Error Exception")

try:
    raise NameError("b. Name Error Exception")
except NameError:
    print("b.Name Error Exception")

"""Generally the except statement takes care of the raised exception - But in case if we need to type any interesting message or alert for the raised exception
we can re raise the exception under Except"""

try:
    raise NameError("c. Name Ereror Exception 01")
except NameError:
    print("c. Name Error Exception 02")
    raise
