# Cart
# - databaseName: string
# - tableName: string
# + Cart():
# + Cart(string databaseName, string tableName)
# + viewCart(string userID, string inventoryDatabase): void
# + addToCart(string userID, string ISBN): void
# + removeFromCart(string userID, string ISBN): void
# + checkOut(string userID): void
# 


import sqlite3
from  inventory import Inventory

def displaySelect(result):
    for tup in result:
        for item in tup:
            print('|', item, '|', end='')
        print()


class Cart:
    def __init__(self, dbName, tblName, connection):
        ## initialize class, database and table name variables and cursor for database
        self.__dbName = dbName
        self.__tblName = tblName
        self.__connection = connection
        self.__cursor = self.__connection.cursor()
        
    def viewCart(self, userID, inventoryTable):
        ## execute query to select the all items tied to userID in cart table\
        self.__cursor.execute(f"SELECT {inventoryTable}.title, {inventoryTable}.author, {self.__tblName}.quantity from {inventoryTable} JOIN {self.__tblName} ON {inventoryTable}.ISBN={self.__tblName}.ISBN WHERE userID={userID}")  # CHANGE ME
        result = self.__cursor.fetchall()
        displaySelect(result)
        
    def addToCart(self, userID, ISBN):
        ## check if is book already in the user's cart
        self.__cursor.execute(f"SELECT * FROM {self.__tblName} WHERE userID='{userID}'")
        check = self.__cursor.fetchall()
        quantity = 1    ## will stay 1 if there is not an entry of the ISBN in the table already
        for tup in check:
            if int(tup[0]) == int(ISBN):
                
                quantity = int(tup[2]) + 1
                # deletes entry
                self.__cursor.execute(f"DELETE FROM {self.__tblName} WHERE userID={userID} AND ISBN={ISBN}")

        ## if the book was in the cart, replaces previous entry with the same with 1+ to the quantity, otherwise
        ## the entry has a quantity of 1
        self.__cursor.execute(f"Insert INTO {self.__tblName} (ISBN, userID, quantity) VALUES ({ISBN},{userID},{quantity})")
        ## commit query
        self.__connection.commit()
        ## print success
        print('successfully added')
        
    def removeFromCart(self, userID, ISBN):
        ## see if the book is already in the cart
        self.__cursor.execute(f"SELECT * FROM {self.__tblName} WHERE userID='{userID}'")
        check = self.__cursor.fetchall()
        for tup in check:
            isThere = False
            if int(tup[0]) == int(ISBN):
                isThere = True
        ## if the book is already in the cart
        quantity = int(tup[2]) - 1
        if isThere and quantity != 0:
            # delete entry and replace with quantity - 1
            self.__cursor.execute(f"DELETE FROM {self.__tblName} WHERE userID={userID} AND ISBN={ISBN}")
            self.__cursor.execute(f"Insert INTO {self.__tblName} (ISBN, userID, quantity) VALUES ({ISBN},{userID},{quantity})")
        ## if the book is not already in the cart
        else:  
            ## delete entry
            self.__cursor.execute(f"DELETE FROM {self.__tblName} WHERE userID={userID} AND ISBN={ISBN}")
        ## commit query
        self.__connection.commit()
        ## print success
        print('successfully deleted')
        
    def checkout(self, userID, inventory):
        self.__cursor.execute(f"SELECT ISBN, quantity FROM {self.__tblName} WHERE userID={userID}")
        decrementList = self.__cursor.fetchall()
        for book in decrementList:
            inventory.decreaseStock(book[0], book[1])
                
        self.__cursor.execute(f"DELETE FROM {self.__tblName} WHERE userID={userID}")
        
        # commit query
        self.__connection.commit()
        # print success
        print('successful checkout')
        
        

