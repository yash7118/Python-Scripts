print("Welcome to Master For Loop Pyramids!")
n =int(input("Enter the value of n"))


def pyramid1():
    print("Printing pyramid 1")
    for i in range(n):
        for j in range(n):
            print(i, end="")
        print()


def pyramid1A():
    print()
    print("Printing pyramid 1A")
    for i in range(n):
        for j in range(i):
            print(i, end="")
        print()


def pyramid2():
    print()
    print("Printing pyramid 2")
    for i in range(n):
        for j in range(i):
            print(j, end="")
        print()

def pyramid3():
    print()
    print("Printing pyramid 2")
    val =0
    for i in range(n):
        for j in range(i):
            print(val, end="")
            val += 1
        print()

def Main():
    pyramid1()
    pyramid1A()
    pyramid2()
    pyramid3()


if __name__ == "__main__":
    Main()