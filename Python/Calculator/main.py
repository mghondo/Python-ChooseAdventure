from Art import calculator_art, calculator_text

def calculator():
    print(calculator_art)
    print(calculator_text)
    print("Welcome to the Calculator!")
    
    # Ask for the first number
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            break
        except ValueError:
            print("Please enter a valid number.")
    
    # Ask for the operation
    while True:
        operation = input("Choose an operation (+ - * /): ")
        if operation in ['+', '-', '*', '/']:
            break
        else:
            print("Please enter a valid operation (+, -, *, or /).")
    
    # Ask for the second number
    while True:
        try:
            num2 = float(input("Enter the second number: "))
            if operation == '/' and num2 == 0:
                print("Error: Cannot divide by zero. Please enter a non-zero number.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")
    
    # Perform the calculation
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    else:  # operation == '/'
        result = num1 / num2
    
    # Display the result
    print(f"\nResult: {num1} {operation} {num2} = {result}")

if __name__ == "__main__":
    calculator()
