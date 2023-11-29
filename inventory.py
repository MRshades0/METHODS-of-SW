import sqlite3

class Inventory:
	def __init__(self, dbName, tName, connection):
		self.__dbName = dbName
		self.__tblName = tName
		self.__connection = connection
		self.__cursor = self.__connection.cursor()

	def viewInventory(self):
		self.__cursor.execute(f'SELECT * FROM {self.__tblName}')
		result = self.__cursor.fetchall()

		for row in result:
			print(row)

	def searchInventory(self):
		title = input('Enter book title: ')
		self.__cursor.execute(f"SELECT * FROM {self.__tblName} WHERE title LIKE '%{title}%'")
		result = self.__cursor.fetchall()
		print()
		for row in result:
			print(row)
		print()

	def decreaseStock(self, ISBN, quantity):
		self.__cursor.execute(f"SELECT stock FROM {self.__tblName} WHERE ISBN='{ISBN}'")
		result = self.__cursor.fetchall()
		newQuantity = int(result[0][0]) - (int(quantity))
		self.__cursor.execute(f"UPDATE {self.__tblName} SET stock = '{newQuantity}' WHERE ISBN='{ISBN}'")
