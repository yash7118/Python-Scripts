from . import NumberProperties as numprop


def Main():
    # This is main function to check module NumberProperties.
    number = int(input("Enter number: "))
    isPrime = numprop.isPrime(number)
    if(isPrime == 1):
        print(str("number") + " is a prime number")
    else:
        print(str("number") + " is a composite number")

if __name__ == "__main__":
    Main()
