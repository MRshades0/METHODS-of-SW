import sqlite3
import sys
import random

try:
    connection = sqlite3.connect("methods.db")

    print("Successful connection.")

except:
    print("Failed connection.")

    ## exits the program if unsuccessful
    sys.exit()

cursor = connection.cursor()

class User:
    dataBaseName = "methods.db"
    tableName = "users"
    loggedIn = False
    userID = ""

    def __init__ (self, dataBaseName = "", tableName = ""):
        self.dataBaseName = dataBaseName
        self.tableName = tableName
        
    def login(self):
        userID = input("Please enter userID: ")
        password = input("Please enter password: ")
        self.loggedIn = True 
    def logout(self):
        self.loggedIn = False
    def viewAccountInformation(self):
        print('First name: ', self.first)
        print('Last name: ',self.last)
        print('Phone number',self.number)
        print('Email Adress: ', self.email)
        print('Full Address: ', self.address, self.city, self.state, self.zip)
    def createAccount(self):
        self.firstName = str(input('What is your first name? '))
        self.lastName = input('What is your last name? ')
        self.number = input('What is your number? ')
        self.email = input('What is your email? ')
        self.address = input('What is you street address (No zip, city, or state)? ')
        self.zip = input('What is your zip code? ')
        self.city = input('What city do you live in? ')
        self.state = input('What state do you live in? ')
        self.password = input('Create a password for your account: ')
        self.UserID = str(random.randit(100000, 999999))

        query = "INSERT INTO users (Last, First, UserID, Number, Email, Address, Zip, City, State, Password) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        data = (self.lastName, self.firstName, self.userID, self.number, self.email, self.address, self.zip, self.city, self.state, self.password)
        cursor.execute(query, data)
        connection.commit()

        print("New User Added")
        print("Your userID is: ", self.userID)

    def getLoggedIn(self):
        return self.loggedIn
    def getUserID(self):
        return self.UserID