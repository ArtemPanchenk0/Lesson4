# Converter
while True:
    answer = input("Enter a number from 1 to 4: ")
    if answer.isdigit():
        answer = int(answer)
    else:
        print("\033[91m" + "Please, enter only integer! String is forbidden!"+ "\033[0m")

    if answer != 1 and answer != 2 and answer != 3 and answer != 4 and type(answer) is int:
        print("\033[91m" + "Incorrect number! You need to enter a number from 1 to 4:" + "\033[0m")

    if answer == 1:
        C = int(input("Enter a C: "))
        F = C * 9 / 5 + 32
        print(str(C) + " C" + " -> " + str(F) + " F")
    if answer == 2:
        F = int(input("Enter a F: "))
        C = (F - 32) * 5 / 9
        print(str(F) + " F" + " -> " + str(C) + " C")
    if answer == 3:
        Ml = int(input("Enter a miles: "))
        Km = Ml * 1.60934
        print(str(Ml) + " miles" + " -> " + str(Km) + " km")
    if answer == 4:
        Km = int(input("Enter a km: "))
        Ml = Km / 1.60934
        print(str(Km) + " km" + " -> " + str(Ml) + " miles")
        #elif answer >= 5:
        #print("\033[91m" + "Incorrect answer! Enter a number from 1 to 4:" + "\033[0m")

    answer = input("Do you want to continue? (y/n) ")

    if answer == "y":
        continue
    if answer == "n":
        print("\033[92m" + "Thanks for using!" + "\033[0m")
        break
    else:
        print("\033[91m" + "Incorrect answer! The app will be closed!" + "\033[0m")
        break
