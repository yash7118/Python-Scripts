"""
One can also have an else block in the try-except block such that if the exception does not occur only in that case the else
block will be executed.
"""
try:
    a = 0/0
except:
    print("a. Exception Handled")
else:
    print("a. Successfully Executed!")


try:
    b = 10/20
except:
    print("b. Exception Handled!")
else:
    print("b. Successfully Executed!")


