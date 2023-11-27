import sqlite3

class Inventory:
	def __init__(self, dbName, tName, connection):
		self.__dbName = dbName
		self.__tblName = tName
		self.__connection = connection
		self.__cursor = self.__connection.cursor()

	def viewInventory(self):
		self.__cursor.execute(f'SELECT * FROM {self.tName}')
		result = self.__cursor.fetchall()

		for row in result:
			print(row)

	def searchInventory(self):
		self.__cursor.execute(f"SELECT * FROM {self.tName} WHERE Title LIKE ?",('%'+ title + '%',})
		result = self.__cursor.fetchall()

		if result:
			for row in result:
				print(row)
		else: print(f"Nothing Found")

	def decreaseStock(self, ISBN, quantity):
		self.__cursor.execute(f"UPDATE {self.tName} SET Stock = Stock - ? WHERE ISBN = ?", (quantity, ISBN))
		if __name__ == "__main__":
			manageInventory = Inventory("inventorydb.db","Inventory")
		while True:
			print("1. View")
			print("2. Search")
			print("3. Decrease")
			print("0. Exit")

			option = int(input("Enter Menu Option: "))

			if option == 1:
				manageInventory.viewInventory()
			elif option == 2:
				search = input("Enter Search: ")
				manageInventory.searchInventory(search)
			elif choice == 3:
				ISBN = Input("Enter ISBN: ")
				quantity = int(input("Enter amount to decrease: "))
				manageInventory.decreaseStock(ISBN, quantity)
			elif choice == 0:
				exit()
			else:
				print("Invalid. Enter a number between 0-3.")
