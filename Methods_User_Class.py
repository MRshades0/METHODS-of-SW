import sqlite3
import sys
import random

 
class User:
    dataBaseName = "methods.db"
    tableName = "users"
    loggedIn = False

    #use query to get and store userID after logged in
    userID = ""

    def __init__ (self, dataBaseName, tableName, connection):
        self.dataBaseName = dataBaseName
        self.tableName = tableName
        self.connection = connection
        self.cursor = self.connection.cursor()
        
    def login(self):
        userID = (input("Please enter userID: "))
        self.userID = userID
        password = input("Please enter password: ")
        queryString = "SELECT Password FROM users WHERE UserID='" + userID + "'"
        self.cursor.execute(queryString)
        self.loggedIn = False
        result = self.cursor.fetchall()
        if (result[0][0] == password):
            self.loggedIn = True 
            print("Login Successful")
        else:
            print("Login invalid")
    def logout(self):
        self.loggedIn = False
    def viewAccountInformation(self):
        if (self.loggedIn == True):
            queryString = "SELECT * FROM users WHERE UserID='" + self.userID + "'"
            self.cursor.execute(queryString)
            result = self.cursor.fetchall()
            for x in result:
                print("Name:", x[1], x[0])
                print("Number:", x[2])
                print("email:", x[3])
                print("Address:", x[4], x[5], ",", x[6], x[7])
                print("userID:", x[9])
    def createAccount(self):
        query = "INSERT INTO users (Last, First, UserID, Number, Email, Address, Zip, City, State, Password) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        first = str(input('What is your first name? '))
        last = input('What is your last name? ')
        number = input('What is your number? ')
        email = input('What is your email? ')
        address = input('What is you street address (No zip, city, or state)? ')
        zip = input('What is your zip code? ')
        city = input('What city do you live in? ')
        state = input('What state do you live in? ')
        password = input('Create a password for your account: ')
        UserID = str(random.randint(100000, 999999))
        data = (last, first, UserID, number, email, address, zip, city, state, password)
        self.cursor.execute(query, data)
        self.connection.commit()

        print("New User Added")
        print("Your userID is: ", UserID)

    def getLoggedIn(self):
        return self.loggedIn
    def getUserID(self):
        return self.userID



