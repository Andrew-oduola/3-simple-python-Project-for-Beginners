# Get the first number
# Get the second number
# Get operator

def add(num1, num2):
    return (num1 + num2)


def sub(num1, num2):
    return (num1 - num2)


def mul(num1, num2):

    return (num1 * num2)


def div(num1, num2):
    if num2 == 0:
        return "Error! Division by Zero"
    return (num1 / num2)

def calculator():
    print('Simple Calculator')
    print("Options: 1. Add 2. Subtract 3. Multiply 4. Divide")

    while True:
        choice = input("Choose an operation (1/2/3/4) or 'q'to quit: ")

        if choice == "q":
            print('Exiting the calculator.')
            break

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input('Enter first number: '))
                num2 = float(input('Enter second number: '))
            except ValueError:
                print("Please enter valid numbers.")
                continue

            if choice == '1':
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {sub(num1, num2)}")
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {mul(num1, num2)}")
            elif choice == '4':
                print(f"Result: {num1} / {num2} = {div(num1, num2)}")

calculator()