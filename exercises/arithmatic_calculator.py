# Helper function to create a border for console output visualization
def separator():
    print(58 * '=')

def get_float_input(prompt):
    while True:
        num = input(prompt) 
        try:
            return float(num) 
        except ValueError:
            print("Invalid input! Please enter a valid number. ⚠")

def get_operator(prompt):
    while True: 
        op = input(prompt)
        if op in ['+', '-', '/', '*']: 
            return op
        print("Invalid operator! Please choose +, -, *, or /. ⚠")


def addition(para1, para2):
    return para1 + para2

def subtraction(para1, para2):
    return para1 - para2

def multiplication(para1, para2):
    return para1 * para2

def division(para1, para2):
    if para2 == 0:
        return "Error (Cannot divide by zero)"
    return para1 / para2

def main():

    separator()
    print("__________________________Calculator______________________\n")

    num1 = get_float_input('Enter first number: ')
    operator = get_operator('Enter the operation you want to perform (+, -, *, /): ')
    num2 = get_float_input('Enter second number: ')

    if operator == '+':
        result = addition(num1, num2)
        print(f"Addition of {num1} and {num2} is: {result}")
    elif operator == '-':
        result = subtraction(num1, num2)
        print(f"Subtraction of {num1} and {num2} is: {result}")
    elif operator == '*':
        result = multiplication(num1, num2)
        print(f"Product of {num1} and {num2} is: {result}")
    elif operator == '/':
        result = division(num1, num2)
        print(f"Division of {num1} and {num2} is: {result}")
            
    separator()


if __name__ == "__main__":
    # Starts the main logic of the program
    main()
