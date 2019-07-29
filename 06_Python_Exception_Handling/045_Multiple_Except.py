"""
A program can have multiple except.
"""

try:
    a = 0/0
except ZeroDivisionError:
    print("Zero Division Error Exception")
except:
    print("Unknown Exception!")

try:
    a = 0/0
except NameError:
    print("Name Error Exception")
except:
    print("Unknown Exception!")

try:
    a = 0/0
except Exception as im:
    print("-", im)