"""
Function for finding and printing fibonacci series up to given number.
"""

def printfibonacci(n):
    series = []
    a,b = 0, 1
    while a<n:
        series.append(a)
        a, b = b, a+b
    print(series)


def getfibonacciseries(seriesUpTo):
    series = []
    a, b = 0, 1
    while a < n:
        series.append(a)
        a, b = b, a + b
    return series


