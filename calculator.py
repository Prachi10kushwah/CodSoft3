#----------------------------- CALCULATOR ------------------------------------#

def add( a, b):
    return a + b

def sub( a, b):
    return a - b

def multi( a, b):
    return a * b       

def div( a, b):
    if b == 0:
        print("Error! Division by zero.")
    return a / b

def percentage(a,b):
    return (a + b)/100

def mod(a,b):
    return a % b

def SI( Per ,Rate, Time):
    return (Per*Rate*Time)/100

def square(a,b):
    return a ** b


def calculator():
    print("\n------- SELECT AN OPERATION -------")
    print("\n1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Percentage")
    print("6. Modulous")
    print("7. Square")
    print("8. Simple Interest")

    choice = input("\nEnter choice ( 1 / 2 / 3 / 4 / 5 / 6 / 7 / 8 ) : ")

    if choice in ['1', '2', '3', '4','5','6','7']:

        number1 = float(input("Enter first number : "))
        number2 = float(input("Enter second number : "))

        if(choice == '1'):
            print("Sum is : ",add(number1,number2))


        elif(choice == '2'):
            print("Difference is : ",sub(number1,number2))

        
        elif(choice == '3'):
            print("Multiplication is : ",multi(number1,number2))

        
        elif(choice == '4'):
            print("Division is : ",div(number1,number2))

        
        elif(choice == '5'):
            print("Percentage is : ",percentage(number1,number2))

        
        elif(choice == '6'):
            print("Modulous is : ",mod(number1,number2))


        elif(choice == '7'):
            print("Square is : ",square(number1,number2))

        else:
            print("Invaild Choice ....")

        
    if choice == '8':
        Per = float(input("Enter Percentage : "))
        Rate = float(input("Enter Rate : "))
        Time = float(input("Enter Time : "))
        print("Simple Interest is : ",SI(Per,Rate,Time))


if __name__== "__main__":
    calculator()





              


