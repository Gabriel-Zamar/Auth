import random


import datetime as dt

database = {
    7304136724: ["dayo", "opaleye", "aaa@abc.com", "password", 10000],
    1: ["Laura", "Apara", "abc@xyz.com", "password", 0]
}

1
def init():
    print("Welcome to Bank Zuri")

    haveAccount = int(input("Do you have an account with us? 1(Yes) 2 (No)"))

    if (haveAccount == 1):

        login()
    elif (haveAccount == 2):

        register()
    else:
        print("Invalid option selected")
        init()


def login():
    print("****Login****")

    AccountNumberFromUser = int(input("Enter your customer number \n"))
    password = input("Please enter your account password \n")


    for AccountNumber, UserDetails in database.items():
        if (AccountNumber == AccountNumberFromUser):
            if (UserDetails[3] == "password"):
                bankOperations(UserDetails)

    print("invalid account number or pin")
    register()


def register():
    print("****Please Register to proceed**** \n")

    email = input("Please enter your email address \n")
    first_name = input("Please enter your First name \n")
    last_name = input("Please enter your Last name \n")
    password = input("Create a password \n")

    AccountNumber = generateAccountNumber()

    database[AccountNumber] = [first_name, last_name, email, password, 0]

    print("Account created successfully")
    print("===  =====  === ==== ====")
    print("Thank-you for banking with us")
    print("**** *** ***** *** ***** ****")
    print("Your account number is: %d" % AccountNumber)
    print("**** *** ***** *** ***** ****")
    print("Do not share your account pin with anyone")
    print("**** *** ***** *** ***** ****")
    print("Please enter your login details to continue your transaction")

    login()


class AccountNumberFromUser:
    pass


def bankOperations(user: object):
    print("Welcome %s %s " % (user[0], user[1]))

    print("**** *** ***** **** ****** ****")
    print("your available balance is %d" % (user[4]))

    current_datetime = dt.datetime.now()
    print(current_datetime)

    selectedoption = int(
        input("what would you like to do? (1) Deposit (2) Withdrawal (3) Transfer (4) Logout (5) Complaint \n"))

    if (selectedoption == 1):
        selectedoption = int(input("How much would you like to deposit? \n"))
        print("Thank-you for banking with us")
        print("**** **** **** **** ****")
        print("Transaction completed successfully")
        print("**** **** **** **** **** ****")
        print("Your available balance is %d" % se)
        print("**** **** **** **** **** **** **** **** ")
        selectedoption = int(input(
            "what else would you like to do? (1) Deposit (2) Withdrawal (3) Transfer (4) Logout (5) Complaint \n"))

        login()
    elif (selectedoption == 2):
        selectedoption = int(input("How much would you like to withdraw? \n"))
        print("Thank-you for banking with us")
        print("**** **** **** **** ****")
        print("Transaction successful")
        print("**** **** **** **** **** ****")
        print("Please take your card")
        print("**** **** **** **** **** **** ****")
        print("Your available balance is %d" % user[4])
        print("**** **** **** **** **** **** **** **** ****")
        selectedoption = int(input(
            "what else would you like to do? (1) Deposit (2) Withdrawal (3) Transfer (4) Logout (5) Complaint \n"))

        login()
    elif (selectedoption == 3):
        selectedoption = int(input("How much would you like to transfer? \n"))

        selectedoption = (input("Enter the recipient account name. \n"))
        selectedoption = int(input("please enter the recipient account no. \n"))
        for AccountNumber, UserDetails in database.items():
            if (AccountNumber == AccountNumberFromUser):
                bankOperations(UserDetails)

            print("Transaction to %s %s" % (user[0], user[1])("is successful"))
        else:
            print("You have entered invalid account information")
            selectedoption = int(
                input("what would you like to do? (1) Deposit (2) Withdrawal (3) Transfer (4) Logout (5) Complaint \n"))

        transferOperation()
    elif (selectedoption == 4):

        logout()

    elif (selectedoption == 5):
        selectedoption = input("What issue would you like to report? \n")
        print("Thank-you for contacting us")
        print("**** **** **** **** **** ****")
        print("We'll get back to you as soon as possible")
        selectedoption = int(input(
            "what else would you like to do? (1) Deposit (2) Withdrawal (3) Transfer (4) Logout (5) Complaint \n"))

        exit()
        print("invalid option selected")
        bankOperations()

    else:
        print("Select a transaction to perform.")
        init()
def withdrawalOperation():
    print("withdrawal")







def depositOperetion():
    print("Deposit")


def transferOperation():
    print("Transfer")


def generateAccountNumber():
    return random.randrange(1111111111, 9999999999)


def set_current_balance(UserDetails, balance):
    UserDetails[4] = balance


def getCurrentAccountBallance(UserDetails):
    return UserDetails[4]


def logout():
    login()


init()
