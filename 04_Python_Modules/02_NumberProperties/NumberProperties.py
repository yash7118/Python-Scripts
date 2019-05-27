"""
Check If Number if Prime or Composite
"""

def isPrime(n):
    a = 2
    counter = 0
    for number in range (a, n):
        if (n % number == 0):
            print("Factor for " +str(n) + " is "+ str(number))
            return 0
    return 1

