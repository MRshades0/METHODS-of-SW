import sqlite3
import sys
import random

 
class User:
    dataBaseName = "methods.db"
    tableName = "USER"
    loggedIn = False

    #use query to get and store userID after logged in
    userID = ""

    def __init__ (self, dataBaseName, tableName, connection):
        self.__dataBaseName = dataBaseName
        self.__tableName = tableName
        self.__connection = connection
        self.__cursor = self.__connection.cursor()
        
    def login(self):
        userID = (input("Please enter userID: "))
        self.userID = userID
        password = input("Please enter password: ")
        queryString = "SELECT P\password FROM USER WHERE userID='" + userID + "'"
        self.__cursor.execute(queryString)
        self.loggedIn = False
        result = self.cursor.fetchall()
        if (result == []):
            print("Login invalid\n")
            return False
        elif (result[0][0] == password):
            self.loggedIn = True 
            print("Login Successful\n")
            return True
        else:
            print("Login invalid\n")
            return False
    def logout(self):
        self.userID = ""
        self.loggedIn = False
        return False
    def viewAccountInformation(self):
        if (self.loggedIn == True):
            queryString = "SELECT * FROM USER WHERE userID='" + self.userID + "'"
            self.__cursor.execute(queryString)
            result = self.__cursor.fetchall()
            for x in result:
                print("Name:", x[1], x[0])
                print("Payment Type:", x[2])
                print("Email:", x[3])
                print("Address:", x[4], x[5], ",", x[6], x[7])
                print("userID:", x[9], "\n")
    def createAccount(self):
        query = "INSERT INTO USER (last, first, userID, payment, email, address, zip, city, state, password) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        first = str(input('What is your first name? '))
        last = input('What is your last name? ')
        payment = input('What payment type will you be using? ')
        email = input('What is your email? ')
        address = input('What is you street address (No zip, city, or state)? ')
        zip = input('What is your zip code? ')
        city = input('What city do you live in? ')
        state = input('What state do you live in? ')
        password = input('Create a password for your account: ')
        UserID = str(random.randint(100000, 999999))
        data = (last, first, UserID, payment, email, address, zip, city, state, password)
        self.__cursor.execute(query, data)
        self.__connection.commit()

        print("New User Added")
        print("Your userID is: ", UserID, "\n")

    def getLoggedIn(self):
        return self.loggedIn
    def getUserID(self):
        return self.userID



