import sqlite3
import sys
import random
from Methods_User_Class import User
from cart_class import Cart

try:
    connection = sqlite3.connect("methods.db")

    print("Successful connection.")

except:
    print("Failed connection.")

    ## exits the program if unsuccessful
    sys.exit()

cursor = connection.cursor()
dataBaseName = "methods.db"
user = User()
cart = Cart()
passed = False
while(passed == False):
    print("1. Login")
    print("2. Create Account")
    print("3. Logout")
    print("\n")
    select = input("Please select option from menu: ")
    if (select == 1):
        if(user.login() == False):
            print("Invalid Login")
        else:
            passed = True
    elif(select == 2):
        user.createAccount()
        passed = True
    elif(select == 3):
        user.logout()
        passed = True
    else:
        print("Invalid menu selection, please try again\n")
passed = False
loggedIn = True
while(loggedIn == True):
    print("Menu:\n1. Logout\n2. View Account Information\n3. Inventory Information\n4. Cart Information")
    select = input("Please select option from menu: ")
    if(select == 2):
        user.viewAccountInformation()
    elif(select == 3):
        inventorySelect = 0
        while(inventorySelect != 1):
            print("Inventory Menu:\n1. Go Back\n2. View Inventory\n3. Search Inventory")
            inventorySelect = input("Select option from inventory menu: ")
            if(inventorySelect == 2):
                #view inventory
            elif(inventorySelect == 3):
                #search inventory
            elif(inventorySelect != 1)
                print("Invalid selection")
    elif(select == 4):
        cartSelect = 0
        while(cartSelect != 1):
            print("Cart Menu:\n1. Go Back\n2. View Cart\n3. Add Items to Cart\n4. Remove an Item from Cart\n5. Check Out")
            cartSelect = input("Select option from cart menu: ")
            if (cartSelect == 2):
                userID = user.getUserID()
                cart.viewCart(userID, #inventoryTable)
            elif(cartSelect == 3)
                #Add items to cart
            elif(cartSelect == 4)
                #Remove items from cart
            elif(cartSelect == 5)
                #checkout
            elif(cartSelect != 1)
                print("Invalid selection")