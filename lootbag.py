import sys
import sqlite3


class Bag:
	def __init__(self):
		pass


	def add_toy_items_to_child(self, child, toy):

		with sqlite3.connect('lootbag.db') as conn:
			c = conn.cursor()

			try:
				c.execute("INSERT INTO Child VALUES (?,?,?)",
					(None, child, 0))
			except sqlite3.OperationalError:
				pass

			c.execute("SELECT c.ChildId, c.Name FROM Child c WHERE Name='{}'".format (child))
			# print(c.fetchall())
			# 
			results = c.fetchall()
			print(results)


			try:
				c.execute("INSERT INTO Toy Values(?,?,?)", (None, toy, results[0][0]))
			except sqlite3.OperationalError:
				pass

			

	def get_by_child(self, child):
		
		with sqlite3.connect('lootbag.db') as conn:
			c = conn.cursor()

			c.execute("SELECT t.Name FROM Toy t, Child c WHERE c.Name='{}' AND c.ChildId = t.ChildId"
				.format(child))
			# print(c.fetchall())
			# 
			toys = c.fetchall()
			print(toys)

	def remove_toy_items(self,child, toy):
		with sqlite3.connect('lootbag.db') as conn:
			c = conn.cursor()
			c.execute("SELECT ChildId FROM Child WHERE Name='{}'".format (child))
			# print(c.fetchall())
			# 
			results = c.fetchall()

			try:
				c.execute("DELETE FROM Toy Where ChildId ={} AND Name='{}'".format(results[0][0],toy) )
			except sqlite3.OperationalError:
				pass

		
	def remove_child_toy(self, child):

		with sqlite3.connect('lootbag.db') as conn:
			c = conn.cursor()
			c.execute("SELECT ChildId FROM Child WHERE Name = '{}'".format(child))
			results = c.fetchall()
			print(results)

			try:
				c.execute("DELETE FROM Child WHERE ChildId = {} ".format(results[0][0]))
			except sqlite3.OperationalError:

				pass

	def get_list_of_kids(self):
		with sqlite3.connect('lootbag.db') as conn:
			c = conn.cursor()
			c.execute("SELECT c.Name FROM Child c")
			results = c.fetchall()
			print(results)
		# return [name for name in self.items.keys()]
		pass

	def is_child_happy(self):
		with sqlite3.connect('lootbag.db') as conn:
			c = conn.cursor()
			c.execute("SELECT ChildId FROM Child c, Toy t WHERE c.ChildId = t.ChildId")
			results = c.fetchall()

			try:
				c.execute("UPDATE c.Happy SET Happy = 1 WHERE c.ChildId = t.ChildId ")
	

if __name__ == "__main__":
	
	bag = Bag()
	
	program_name = sys.argv[0]
	print(program_name)
	arguments = sys.argv[1:]
	
	if arguments[0] == "add":
		# print(bag.add_toy_items_to_child("Holly", "kitchen-set"))
		bag.add_toy_items_to_child(arguments[1],arguments[2])

	if arguments[0] == "ls":
	   bag.get_list_of_kids()

	if arguments[0] == "remove":
		bag.remove_toy_items(arguments[1], arguments[2])

	if arguments[0] == "delete":
		bag.remove_child_toy(arguments[1])

	if arguments[0] == "toys":
		bag.get_by_child(arguments[1])

	if arguments[0] == "append":
		bag.add_toy_items_to_child(arguments[1], arguments[2])


	