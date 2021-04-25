import random
import datetime
from db import bankUsers

time = datetime.datetime.now()


def landingpage():
    print("Hello. Enter 1 to login or 2 to register")
    option = int(input("1. Login \n 2. Register \n Input:   "))

    if option == 1:
        login()
    elif option == 2:
        register()
    else:
        print("Invalid option")

def bankOperations():

    isvalid_input = True

    while isvalid_input:

        print('\nLogin Succesful \n')
        print('1. Withdrawal\n')
        print('2. Cash Deposit\n')
        print('3. Complaint\n')

        selectedOption = int(input('Please select an option:    '))

        if selectedOption in range(1,4):      
            if(selectedOption == 1):
                withdrawal()
                
            elif(selectedOption == 2):
                pass
                        
            elif(selectedOption == 3):
                pass             
        else:
            print('Invalid Option selected\n')
            isvalid_input = False
            retry_options = int(input('Would you like to try again?\n 1. Yes \n 2. No \n Enter 1 or 2:  '))
            if retry_options in range(1,3):
                if retry_options == 1:
                    isvalid_input = True
    else:
        print('\nGoodbye')

def withdrawal():
    
    amount = float(input("How much would you like to withdrawal?    "))
    print('processing..')
    print('take your cash')  

def register():
    print("Welcome to new age bank registration platform")
    print("To register please fill in the following questions")
    firstName = str.lower(input("What is your First name :   "))
    lastName = str.lower(input("What is your last name :   "))
    bvn = int(input("What is your bank registration number (BVN) :   "))
    generateNumber = [random.randint(0,10) for x in range(10)]      
    accountNumber = ''.join([str(item) for item in generateNumber])
    password = int(input("Enter a 4 digit password:   "))

    print(f"Hello {firstName} {lastName} your account number is {accountNumber} and {password} is your password")

    createUser(firstName,lastName,bvn,accountNumber,password)
    login()
    

def createUser(firstName,lastName,bvn,accountNumber,password):
    bankUsers[accountNumber] = {}

    bankUsers[accountNumber]["First Name"] = firstName
    bankUsers[accountNumber]["Last Name"] = lastName
    bankUsers[accountNumber]["BVN"] = bvn
    bankUsers[accountNumber]["Account Number"] = accountNumber
    bankUsers[accountNumber]["Password"] = password
    bankUsers[accountNumber]["Date created"] = time.strftime("%c")
    
    
def login():
    print("Login to new age bank")
    accountNumber = int(input("Please enter your account number:    "))
    pin = int(input("Please enter your secret pin:    "))

    if accountNumber in bankUsers:
        if bankUsers[accountNumber][Password] == pin:
            bankOperations()
    else:
        print("Account invalid")
        landingpage()
                   
landingpage()