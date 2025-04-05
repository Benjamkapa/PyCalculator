import time
import math
history = []

def sqrt(a):
    return math.sqrt(a)

def add(a, b):
    return a + b

def minus(a, b):
    return a - b

def times(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def modulus(a, b):
    return a % b

def power(a, b):
    return a ** b

def square(a):
    return a ** 2

def get_positive_number(prompt):
    while True:
        value = input(prompt).strip()
        if not value:
            print("Input cannot be empty. Please try again.")
            continue
        try:
            num = float(value)
            if num < 0:
                print("Number must be positive. Please try again.")
                continue
            return num
        except ValueError:
            print("Invalid number. Please enter a valid number.")

while True:
    print("\n******************************")
    print("Welcome to Benja's Calculator")
    print("******************************\n")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Square Root")
    print("8. Square")  # Added Square option here
    print("9. Exit")
    print("10. History")

    choice = input("\nEnter your choice (1–10): ").strip()

    if choice == '9':
        print("\nExiting and saving history...\n")
        with open("calc_history.txt", "w") as file:
            for entry in history:
                file.write(entry + "\n")
        print("History saved to calc_history.txt")
        break

    elif choice == '10':
        if history:
            print("\n--- Calculation History ---")
            for entry in history:
                print(entry)
        else:
            print("No history yet.")
        continue  # Go back to menu

    elif choice not in ['1', '2', '3', '4', '5', '6', '7', '8']:
        print("Invalid choice. Please try again.")
        continue

    num1 = get_positive_number("Enter the first number: ")
    
    # For square root and square, we only need one number
    if choice not in ['7', '8']:
        num2 = get_positive_number("Enter the second number: ")

    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    if choice == '1':
        result = add(num1, num2)
        operator = '+'
    elif choice == '2':
        result = minus(num1, num2)
        operator = '-'
    elif choice == '3':
        result = times(num1, num2)
        operator = '*'
    elif choice == '4':
        result = divide(num1, num2)
        operator = '/'
    elif choice == '5':
        result = modulus(num1, num2)
        operator = '%'
    elif choice == '6':
        result = power(num1, num2)
        operator = '^'
    elif choice == '7':
        result = sqrt(num1)
        operator = 'sqrt'
        num2 = None  # No second number for square root operation
    elif choice == '8':  # Square operation
        result = square(num1)
        operator = 'square'
        num2 = None  # No second number for square operation

    print(f"\nThe result is: {result}")
    print("---------------------------\n")
    
    # History entry for square and square root operations (no num2)
    if choice in ['7', '8']:
        history_entry = f"[{timestamp}] {operator} {num1} = {result}"
    else:
        history_entry = f"[{timestamp}] {num1} {operator} {num2} = {result}"
    
    history.append(history_entry)

    # Ask if user wants to perform another operation
    while True:
        again = input("Do you want to perform another operation? (y/n): ").strip().lower()
        if again == 'y':
            break
        elif again == 'n':
            print("\nExiting and saving history...\n")
            with open("calc_history.txt", "w") as file:
                for entry in history:
                    file.write(entry + "\n")
            print("History saved to calc_history.txt")
            exit()
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
