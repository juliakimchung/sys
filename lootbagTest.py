import unittest
from lootbag import *

def setUpModule():
	print("set up module for lootbagTest.py")

def tearDownModule():
	print("tear down module for lootbagTest.py")

class testLootbag(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		self.bag = Bag()
		print("set up class for testLootbag class")
		

	@classmethod
	def tearDownClass(self):
		print("tear down class")



	# def test_lootbagMustHaveNameProperty(self):
		
	# 	self.bag.add_name("Suzy")
	# 	self.assertEqual(self.bag.name, {"Suzy"})

	# def test_lootbagMustHaveToyProperty(self):

	# 	self.bag.add_toy("train")
	# 	self.assertEqual(self.bag.toy, {"train"})

	def test_lootbagMustHaveItems(self):
		self.bag.add_toy_items_to_child("Remi", "computer")
		self.assertIn("computer", self.bag.items['Remi'])

	def test_remove_child_toy(self):
		self.bag.add_toy_items_to_child("Tammy", "dolls")
		self.bag.remove_child_toy("Tammy")
		self.assertNotIn("Tammy", self.bag.items )

	def test_get_list_of_kids(self):
		self.bag.get_list_of_kids()
		self.assertEqual([name for name in self.bag.items.keys()], self.bag.get_list_of_kids())
	def test_get_by_child(self):
		self.bag.get_by_child("Madison")
		self.assertEqual(self.bag.items["Madison"],self.bag.get_by_child("Madison"))

	def test_is_delievered(self):
		self.assertFalse(bag.is_child_happy("Remi"))
		self.bag.delivery_done("Remi")
		self.assertTrue(bag.is_child_happy("Remi"))


if __name__ == '__main__':
	unittest.main()