# TEST CASES SignIn for the  LOGIN/PASSWORD feature
# Valid	login = Test
# valid password = T@2024
# if login = Test and password = T@2024 than Test was passed!
# if (login and password) or (login or password) isn't valid that
# error message on display: Provide valid combination!
login = input("Enter your login: ")
password = input("Enter your password: ")
def print_signin():
    if login == "Test" and password == "T@2024":
        print(" ")
        print("Your data is valid: " + "login = " + login)
        print("                    " + "password = " + password)
        print(" ")
        print(cred + "Test was passed!" + cend)

    else:
        print(" ")
        print(cred + "Provide valid combination!" + cend)
        print(" ")
        # print("Test was passed!")


cred = "\033[91m"
cend = "\033[0m"
login = input("Enter your login: ")
password = input("Enter your password: ")
print_signin()


