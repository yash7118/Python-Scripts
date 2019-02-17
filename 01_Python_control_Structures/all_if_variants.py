num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
    print(str(num1) + " is greater than "+ str(num2))
    print("The difference is"+ str(num1-num2))
elif num1 < num2:
    print(str(num2)+" is greater than "+str(num1))
    print("The difference is "+str(num2-num1))
else:
    print(str(num1)+ " is equal to "+ str(num2))
    print("The difference is: "+str(num1-num2))