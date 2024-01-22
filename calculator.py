# Design a simple calculator with basic arithmetic operations.
# Prompt the user to input two numbers and an operation choice.

# Perform the calculation and display the result.

while(1):
    print("                CALCULATOR                ")
    print("---------------************---------------")

    num1=int(input("Enter the first number :"))
    print("\n")
    num2=int(input("Enter the second number:"))
    print("\n")
    print("Select the desired operation for the choices mentioned below")
    print("\n")
    print("1-->Addition\n\n2-->Subtraction\n\n3-->Multiplication\n\n4-->Division\n\n5-->Exponential or Power")
    print("\n")
    choice=int(input("Enter your choice according to the operation you want to perform :"))
    print("\n")
    if choice==1:
        result=num1+num2
        print(f"The Addition of the Two provided numbers {num1} and {num2} is : {result}")

    elif choice==2:
        result=num1-num2
        print(f"The Subtraction of the Two provided numbers {num1} and {num2} is : {result}")

    elif choice==3:
        result=num1*num2
        print(f"The Multiplication of the Two provided numbers {num1} and {num2} is : {result}")

    elif choice==4:
        if num2==0:
            print("The Denominator value is a '0' , Further Operation cannot be performed ")
            continue
        result=num1/num2
        print(f"The Division of the Two provided numbers {num1} and {num2} is : {result}")

    elif choice==5:
        result=num1**num2
        print(f"The Power of First number to the Second number {num1} and {num2} is  : {result}")

    else:
        print("The Choice entered is Invalid")
    print("\n")
    stop=input("Enter your choice to continue (y/n) :")
    if stop=="n":
        break
    else:
        continue