# TEST CASES SignIn for the  LOGIN/PASSWORD feature
# Precondition: valid login = Test, valid password = T@2024
# if login = Test and password = T@2024 than Test was passed!
# if (login and password) or (login or password) isn't valid that
# will be error message on display: Provide valid combination!
# and User need to type new valid login and password

sred = "\033[91m"
send = "\033[0m"
login = input("Enter your login: ")
password = input("Enter your password: ")

while ((login != "Test" and password != "T@2024")
       or (login != "Test" and password == "T@2024")
       or (login == "Test" and password != "T@2024")):
    print(" ")
    print(sred + "Provide valid combination!" + send)
    print(" ")
    print(" ")
    if login != "Test" and password != "T@2024":
        login = input("Enter your valid login: ")
        password = input("Enter your valid password: ")
    elif login != "Test" and password == "T@2024":
        print("Your password is valid: " + "password = " + password)
        login = input("Enter your valid login: ")
    elif login == "Test" and password != "T@2024":
        print("Your login is valid: " + "login = " + login)
        password = input("Enter your valid password: ")

else:
    print(" ")
    print("Your data is valid: " + "login = " + login)
    print("                    " + "password = " + password)
    print(" ")
    print(sred + "Test was passed!" + send)
