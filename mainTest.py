import sqlite3
import sys
import random
from Methods_User_Class import User

try:
    connection = sqlite3.connect("methods.db")

    print("Successful connection.")

except:
    print("Failed connection.")

    ## exits the program if unsuccessful
    sys.exit()

cursor = connection.cursor()
dataBaseName = "methods.db"
tableName = "users"
test = User(dataBaseName, tableName, connection)
#test.createAccount()
test.login()
if(test.getLoggedIn == True):
    print("Login works")
#test.viewAccountInformation()
test.logout()
loggedIn = test.getLoggedIn()
if (loggedIn == False):
    print("Logout Successful")


