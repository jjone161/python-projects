# Let's build a calculator for our user to use

# addition function
def addition_func(a, b):
    return a + b

# subtraction function
def subtract_func(a, b):
    return a - b

# multiplication function
def multiply_func(a, b):
    return a * b

# division function
def divide_func(a, b):
    return a / b

# variable for the loop
running = True

# while loop for user to choose operation, or quit the game
while running == True:
    user_choice = int(input("Hi there! choose 1 to add, 2 to subtract, 3 to multiply, 4 to divide, or 5 to quit: "))
    if user_choice == 1:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = addition_func(num1, num2)
        print(result)

    elif user_choice == 2:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = subtract_func(num1, num2)
        print(result)

    elif user_choice == 3:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = multiply_func(num1, num2)
        print(result)

    elif user_choice == 4:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = divide_func(num1, num2)
        print(result)
    
    else:
        print("Goodbye, see you next time")
        running = False