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

	def searchInventory(self,):
		self.__cursor.execute;{f"SELECT * FROM {self.tName} WHERE Title LIKE ?",('%'+ title + '%',)}
		result = self.__cursor.fetchall()

		if result:
			for row in result:
				print(row)
		else: print(f"Nothing Found")

	def decreaseStock(self, ISBN, quantity):
		self.__cursor.execute(f"UPDATE {self.tName} SET Stock = '{quantity}'")
