import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))
import unittest
from DictsOrganizations.HashTable import HashTable
from DictsOrganizations.HashTable import HashTableItem


class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.test_common_table = HashTable(3, 4)
        self.test_common_table.add(HashTableItem("ASUS", 80000))
        self.test_common_table.add(HashTableItem("Lenovo", 70000))
        self.test_common_table.add(HashTableItem("HP", 75000))

    def test_add(self):
        self.assertEquals(len(self.test_common_table.hash_table[0]), 4)
        self.assertEquals(len(self.test_common_table.hash_table[1]), 4)
        self.assertEquals(len(self.test_common_table.hash_table[2]), 4)
        self.test_common_table.add(HashTableItem("Apple", 100000))
        self.test_common_table.add(HashTableItem("Dell", 90000))
        self.test_common_table.add(HashTableItem("Acer", 75000))
        self.test_common_table.add(HashTableItem("Toshiba", 65000))
        self.test_common_table.add(HashTableItem("MSI", 55000))
        self.test_common_table.add(HashTableItem("Samsung", 75000))
        self.assertEquals(self.test_common_table.engaged, 12)
        self.assertEquals(len(self.test_common_table.hash_table[0]), 8)
        self.assertEquals(len(self.test_common_table.hash_table[1]), 8)
        self.assertEquals(len(self.test_common_table.hash_table[2]), 8)

    def test_remove(self):
        self.test_common_table.remove("ASUS")
        self.assertEquals(self.test_common_table.search("ASUS"), None)
        self.assertEquals(self.test_common_table.engaged, 5)
        self.test_common_table.remove("Dell")
        self.assertEquals(self.test_common_table.search("Dell"), None)
        self.assertEquals(self.test_common_table.engaged, 4)


if __name__ == "__main__":
    unittest.main()
