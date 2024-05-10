while True:

    while first_number.isdigit() and second_number.isdigit():
        first_number = input("Enter first number: ")
        second_number = input("Enter second number: ")
        if not first_number.isdigit() and not second_number.isdigit():
            print("\033[91m" + "Please, enter only integer! String is forbidden!" + "\033[0m")
            operation = input("Enter operation: ")

        elif first_number.isdigit() and second_number.isdigit():
            first_number = int(input("Enter first number: "))
            second_number = int(input("Enter second number: "))
            operation = input("Enter operation: ")
        #break
        #first_number = input("Enter a number from 1 to 4: ")
