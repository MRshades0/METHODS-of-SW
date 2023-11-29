import sqlite3
import sys
import random
from Methods_User_Class import User
from cart_class import Cart
from inventory import Inventory

def main():
    try:
        connection = sqlite3.connect("methods.db")

        print("Successful connection.")

    except:
        print("Failed connection.")

        ## exits the program if unsuccessful
        sys.exit()

    user = User("methods.db", "USER", connection)
    cart = Cart("methods.db", "CART", connection)
    inventory = Inventory("methods.db", "INVENTORY", connection)
    passed = False
    while(passed == False):
        print("1. Login")
        print("2. Create Account")
        print("3. Logout")
        print()
        select = input("Please select option from menu: ")
        print()
        if (select == '1'):
            if(user.login() == False):
                print("Invalid Login")
            else:
                passed = True
        elif(select == '2'):
            user.createAccount()
            if(user.login() == False):
                print("Invalid Login")
            else:
                passed = True
            
        elif(select == '3'):
            user.logout()
            passed = True
            sys.exit()
        else:
            print("Invalid menu selection, please try again\n")
            
            
    passed = False
    loggedIn = True
    while(loggedIn == True):
        print("Menu:\n1. Logout\n2. View Account Information\n3. Inventory Information\n4. Cart Information")
        select = input("Please select option from menu: ")
        print()
        if select == '1':
            loggedIn = False
        elif(select == '2'):
            user.viewAccountInformation()
        elif(select == '3'):
            inventorySelect = 0
            while(inventorySelect != '1'):
                print("Inventory Menu:\n1. Go Back\n2. View Inventory\n3. Search Inventory\n4. Decrease Stock")
                inventorySelect = input("Select option from inventory menu: ")
                print()
                if(inventorySelect == '2'):
                    inventory.viewInventory()
                elif(inventorySelect == '3'):
                    inventory.searchInventory()
                elif(inventorySelect == '4'):
                    ISBN = input('ISBN of book you wish to decrease the stock of: ')
                    quantity = input('By how much? ')
                    inventory.decreaseStock(ISBN, quantity)
                elif(inventorySelect != '1'):
                    print("Invalid selection")
                print()


        elif(select == '4'):
            cartSelect = 0
            while(cartSelect != '1'):
                print("Cart Menu:\n1. Go Back\n2. View Cart\n3. Add Items to Cart\n4. Remove an Item from Cart\n5. Check Out")
                cartSelect = input("Select option from cart menu: ")
                print()
                if (cartSelect == '2'):
                    userID = user.getUserID()
                    cart.viewCart(userID, 'inventory')
                elif(cartSelect == '3'):
                    userID = user.getUserID()
                    ISBN = input('ISBN of book you wish to add: ')
                    cart.addToCart(userID, ISBN)
                elif(cartSelect == '4'):
                    userID = user.getUserID()
                    ISBN = input('ISBN of book you wish to remove: ')
                    cart.removeFromCart(userID, ISBN)
                elif(cartSelect == '5'):
                    userID = user.getUserID()
                    cart.checkout(userID, inventory)
                elif(cartSelect != '1'):
                    print("Invalid selection")
                print()
main()