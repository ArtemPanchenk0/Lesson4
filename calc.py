# Calc
result = None
while True:
    first_number = input("Enter first number: ")
    second_number = input("Enter second number: ")
    if first_number.isdigit() and second_number.isdigit():
        first_number = int(first_number)
        second_number = int(second_number)
        operation = input("Enter operation: * - / +   ")
        if operation != "*" and operation != "/" and operation != "+" and operation != "-":
            print("\033[91m" + "Incorrect operations, please select the correct operation" + "\033[0m")
            break
    else:
        print("\033[91m" + "Please, enter only integer! String is forbidden!" + "\033[0m")
        break

    if operation == "+":
        result = first_number + second_number
    if operation == "-":
        result = first_number - second_number
    if operation == "*":
        result = first_number * second_number
    if operation == "/":
        if second_number != 0:
            result = first_number / second_number
        else:
            print("\033[91m" + " Error - Division by zero is prohibited! " + "\033[0m")
    print(result)

    answer = input("Do you want to continue? (y/n) ")
    if answer == "y":
        continue
    if answer == "n":
        print("\033[92m" + "Thanks for using!" + "\033[0m")
        break
    else:
        print("\033[91m" + "Incorrect answer! The app will be closed!" + "\033[0m")
        break