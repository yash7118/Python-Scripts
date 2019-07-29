"""
Finally block is always always executed if mentioned.
"Always" as in - irrespective of Exception occurs or not.

Finally block is usually used to clean up the code - that is like closing the file that was opened up in the try block.
"""
try:
    a = 0/0
except:
    print("a. Exception Handled")
else:
    print("a. Successfully Executed!")
finally:
    print ("a. Finally - Code cleanup here")


try:
    b = 10/20
except:
    print("b. Exception Handled!")
else:
    print("b. Successfully Executed!")
finally:
    print("b. Finally - Code cleanup here")


