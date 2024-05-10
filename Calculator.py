first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
operation = input("Enter operation: ")
result = None

# Add loop and ask to continue or quit
if operation == "+":
    result = first_number + second_number
elif operation == "-":
    result = first_number - second_number
elif operation == "*":
    result = first_number * second_number
elif operation == "/":
    if second_number != 0:
        result = first_number / second_number
    else:
        print("\033[91m" + "Division by zero is prohibited!" + "\033[0m")
else:
    print("Invalid operation")

print(result)

answer = input("Do you want to continue? (y/n) ")
while answer == "y":
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    operation = input("Enter operation: ")
    result = None

    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "*":
        result = first_number * second_number
    elif operation == "/":
        if second_number != 0:
            result = first_number / second_number
        else:
            print("\033[91m" + "Division by zero is prohibited!" + "\033[0m")
    else:
        print("Invalid operation")
    if answer == "n":
        break

    print(result)
    answer = input("Do you want to continue? (y/n) ")

# Convert C -> F , F -> C, miles -> km, km -> miles
# 1. C -> F ,
# 2. F -> C,
# 3. miles -> km,
# 4. km -> miles
