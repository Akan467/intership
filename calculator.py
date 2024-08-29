# Design a simple calculator with basic arithmetic operations. 
# Prompt the user to input two numbers and an operation choice.
# perform the calculation and display the result.


print("Please enter two numbers:")
x = int(input("enter first number: "))
y = int(input("enter second number: "))

a = max(x, y)
b = min(x, y)


def addition():
    add = a + b
    print(f"addition of {a} and {b} is {add}")

def substraction():
    sub = a - b
    print(f"substraction of {a} and {b} is {sub}")

def multiplication():
    mul = a * b
    print(f"multiplication of {a} and {b} is {mul}")

def division():
    div = a / b
    print(f"Divison of {a} and {b} is {div}")

def modulus():
    mod = a % b
    print(f"modulus of {a} and {b} is {mod}")
    
if __name__ == "__main__":

   while True:
    print("\n")
    print("Please select one of the following options")
    print("------------------------------------------")
    print("1. Addition:")
    print("2. Substraction:")
    print("3. Multiplication:")
    print("4. Divison:") 
    print("5. Modulus:")        
    print("6. Exit")
    choice = input("Enter your choice (in numbers): ")
    if (choice == "1"):
        addition()

    elif (choice == "2"):
        substraction()

    elif (choice == "3"):
        multiplication()

    elif (choice == "4"):
        division()

    elif (choice == "5"):
        modulus()

    else:
        print("Invalid input. Please try again.")



    