# A simple Python calculator to perform basic arithmetic operations.

# Welcome message
print("Welcome to the Simple Python Calculator!")

while True:
    # Get user input for the first number
    userInput1 = int(input("Enter the first number: "))

    # Get user input for the operation
    oper = input("Enter the operation you would like to perform [+, -, *, /]: ")

    # Get user input for the second number
    userInput2 = int(input("Enter the second number: "))

    # Perform the calculation based on the user's choice
    if oper == "+":
        result = str(userInput1 + userInput2)
        print(f"Your result is: {result}")
    elif oper == "-":
        result = str(userInput1 - userInput2)
        print(f"Your result is: {result}")
    elif oper == "*":
        result = str(userInput1 * userInput2)
        print(f"The result of multiplication is: {result}")
    elif oper == "/":
        # Check for division by zero
        if userInput2 != 0:
            result = userInput1 / userInput2
            print(f"The result of division is: {result}")
        else:
            print("Error: Cannot divide by zero.")
    else:
        print("Invalid operator. Please enter +, -, *, or /.")
    
    rerun = input("Do you want to perform another operation? (Yes/No): ")
    if rerun.lower() != "yes":
        # Provide a friendly closing message
        print("Thank you for using the Simple Python Calculator!")
        break
    