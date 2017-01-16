import sys
import pickle



class Bag:
	def __init__(self):
		self.name = set()
		self.toy = set()
		# self.items = dict()
		self.deserialize()


	def add_name(self, new_name):
		self.name.add(new_name)

	def add_toy(self, new_toy):
		self.toy.add(new_toy)

	def remove_name(self, name_to_remove):
		self.name.remove(name_to_remove)

	def remove_toy(self, toy_to_remove):
		self.toy.remove(toy_to_remove)

	def add_toy_items_to_child(self, name, toy):
		self.items.update({name: toy})
		self.serialize()
		print(self.items)
	def remove_toy_items(self,name):
		del self.items[name]
		self.serialize()

	def serialize(self):
		with open('lootbag.txt', "wb+") as lootbag:
			pickle.dump(self.items, lootbag)
		"""save files"""
	def deserialize(self):
		"""to open files"""
		with open('lootbag.txt', "rb+") as lootbag:
			self.items = pickle.load(lootbag)
		

if __name__ == "__main__":
	
	bag = Bag()
	
	program_name = sys.argv[0]
	print(program_name)
	arguments = sys.argv[1:]
	
	if arguments[0] == "add":
		# print(bag.add_toy_items_to_child("Holly", "kitchen-set"))
		bag.add_toy_items_to_child(arguments[1],arguments[2])

	if arguments[0] == "ls":
	   print(bag.items)

	# bag.add_name("Suzy")
	# bag.add_name("Kyle")
	# bag.add_name("Lily")
	# bag.add_name("Phil")

	# bag.add_toy("kite")
	# bag.add_toy("car")
	# bag.add_toy("kitchen")
	# bag.add_toy("paint")

	# bag.add_toy_items_to_child("Madison", "books")
	# bag.add_toy_items_to_child("Ava", "stickers")
	# bag.add_toy_items_to_child("Olivia", "stickers")
	# print(bag.items)

	# # Bag.remove_toy_items(("Ava", "stickers"))
	# # print(Bag.items)

	# print(bag.remove_toy_items("Olivia"))
	# print(bag.items)
	# print(bag.name)
	# print(bag.toy)