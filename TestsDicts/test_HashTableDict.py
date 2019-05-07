import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))
from Dicts.DictsOrganizations.HashTable import HashTable
from Dicts.DictsOrganizations.HashTable import HashTableItem
from Dicts.TypesDicts.HashTableDict import HashTableDict


class TestAVLTreeDict(unittest.TestCase):
    def setUp(self):
        self.test_common_dict = HashTableDict([("Lenovo", 70000),
                                               ("Toshiba", 65000),
                                               ("Philips", 50000),
                                               ("Vaio", 90000),
                                               ("Samsung", 80000),
                                               ("Dell", 85000),
                                               ("Apple", 100000),
                                               ("HP", 70000), ("Acer", 75000)])
        self.test_little_dict = HashTableDict([("Lenovo", 70000),
                                               ("Philips", 50000),
                                               ("Vaio", 90000), ("HP", 60000),
                                               ("Apple", 100000)])
        self.test_empty_dict = HashTableDict([])

    def test_contains(self):
        self.assertEquals(self.test_common_dict.__contains__("Dell"), True)
        self.assertEquals(self.test_little_dict.__contains__("Acer"), False)

    def test_clear(self):
        test_clear = HashTableDict([("Lenovo", 70000), ("Philips", 50000),
                                    ("Vaio", 90000), ("HP", 70000),
                                    ("Apple", 100000)])
        test_clear.clear()
        self.assertEquals(test_clear.engaged, test_clear.size_height)

    def test_fromkeys(self):
        keys = []
        values = []
        sequence = ["1", "2", "3"]
        test_fromkeys_dict = HashTableDict([("ASUS", 80000),
                                            ("Toshiba", 65000),
                                            ("Dell", 90000), ("Acer", 75000),
                                            ("Apple", 100000),
                                            ("Samsung", 60000)])
        test_fromkeys_dict.fromkeys(sequence, 1)
        founded = 0
        flag = False
        for j in range(1, test_fromkeys_dict.size_width):
            for i in range(test_fromkeys_dict.size_height):
                item = test_fromkeys_dict.hash_table[i][j]
                if item is not None:
                    founded += 1
                    keys.append(item.key)
                    values.append(item.value)
                    if founded == test_fromkeys_dict.engaged:
                        flag = True
                        break
            if flag:
                break
        self.assertEquals("1" in keys, True)
        self.assertEquals("2" in keys, True)
        self.assertEquals("3" in keys, True)
        self.assertEquals(values, [1, 1, 1])

    def test_items(self):
        self.assertEquals(
            ("Lenovo", 70000) in self.test_little_dict.items(), True)
        self.assertEquals(
            ("Philips", 50000) in self.test_little_dict.items(), True)
        self.assertEquals(
            ("Vaio", 90000) in self.test_little_dict.items(), True)
        self.assertEquals(
            ("HP", 60000) in self.test_little_dict.items(), True)
        self.assertEquals(
            ("Apple", 100000) in self.test_little_dict.items(), True)
        self.assertEquals(len(self.test_little_dict.items()), 5)
        self.assertEquals(self.test_empty_dict.items(), [])

    def test_keys(self):
        self.assertEquals("Lenovo" in self.test_little_dict.keys(), True)
        self.assertEquals("Philips" in self.test_little_dict.keys(), True)
        self.assertEquals("Vaio" in self.test_little_dict.keys(), True)
        self.assertEquals("HP" in self.test_little_dict.keys(), True)
        self.assertEquals("Apple" in self.test_little_dict.keys(), True)
        self.assertEquals(len(self.test_little_dict.keys()), 5)
        self.assertEquals(self.test_empty_dict.keys(), [])

    def test_get(self):
        self.assertEquals(self.test_common_dict.get("Lenovo"), 70000)
        self.assertEquals(self.test_little_dict.get("MIO", 45000), 45000)

    def test_popitem(self):
        test_popitem_dict = HashTableDict([("ASUS", 80000), ("Toshiba", 65000),
                                           ("Dell", 90000)])
        test_popitem_dict.popitem()
        self.assertEquals(test_popitem_dict.engaged, 12)
        test_popitem_dict.clear()
        with self.assertRaises(KeyError):
            test_popitem_dict.popitem()

    def test_setdefault(self):
        test_setdefault_dict = HashTableDict([("ASUS", 80000),
                                              ("Toshiba", 65000),
                                              ("Dell", 90000)])
        self.assertEquals(test_setdefault_dict.setdefault("Dell"), 90000)
        self.assertEquals(
            test_setdefault_dict.engaged - test_setdefault_dict.size_height, 3)
        self.assertEquals(test_setdefault_dict.setdefault("MSI", 45000), 45000)
        self.assertEquals(
            test_setdefault_dict.engaged - test_setdefault_dict.size_height, 4)

    def test_pop(self):
        test_pop_dict = HashTableDict([("ASUS", 80000), ("Toshiba", 65000),
                                       ("Dell", 90000)])
        self.assertEquals(test_pop_dict.pop("Toshiba"), 65000)
        self.assertEquals(test_pop_dict.__contains__("Toshiba"), False)
        self.assertEquals(test_pop_dict.engaged - test_pop_dict.size_height, 2)

    def test_values(self):
        self.assertEquals(70000 in self.test_little_dict.values(), True)
        self.assertEquals(50000 in self.test_little_dict.values(), True)
        self.assertEquals(100000 in self.test_little_dict.values(), True)
        self.assertEquals(90000 in self.test_little_dict.values(), True)
        self.assertEquals(60000 in self.test_little_dict.values(), True)
        self.assertEquals(len(self.test_little_dict.values()), 5)
        self.assertEquals(self.test_empty_dict.values(), [])

    def test_update(self):
        test_update_dict = HashTableDict([("ASUS", 80000), ("Apple", 100000),
                                          ("Dell", 90000)])
        test_update_dict.update(self.test_little_dict)
        self.assertEquals(test_update_dict.__contains__("Vaio"), True)
        self.assertEquals(len(test_update_dict), 7)

    def test_copy(self):
        test_copy_dict = self.test_common_dict.copy()
        self.assertEquals(
            test_copy_dict.items(), self.test_common_dict.items())

    def test_eq(self):
        # test_eq_dict = HashTableDict([("Lenovo", 70000), ("Philips", 50000),
        #                               ("Vaio", 90000), ("HP", 70000),
        #                               ("Apple", 100000)])
        # self.assertEquals(self.test_little_dict.__eq__(test_eq_dict), True)
        test_eq_dict = HashTableDict([("ASUS", 80000), ("Toshiba", 65000),
                                      ("Dell", 90000), ("Acer", 75000),
                                      ("Apple", 100000)])
        self.assertEquals(self.test_common_dict.__eq__(test_eq_dict), False)
        test_eq_dict = HashTableDict([("ASUS", 80001), ("Toshiba", 65001),
                                      ("Dell", 90001), ("Acer", 75001),
                                      ("Apple", 100001), ("Samsung", 60001)])
        self.assertEquals(self.test_common_dict.__eq__(test_eq_dict), False)
        test_eq_dict = HashTableDict([("Toshiba", 65000), ("Samsung", 60000),
                                      ("Dell", 90000), ("Apple", 100000),
                                      ("Acer", 75000), ("ASUS", 80000)])
        self.assertEquals(self.test_common_dict.__eq__(test_eq_dict), False)

    def test_len(self):
        self.assertEquals(0, self.test_empty_dict.__len__())
        self.assertEquals(9, self.test_common_dict.__len__())
        self.assertEquals(5, self.test_little_dict.__len__())

    def test_delitem(self):
        test_delitem_dict = HashTableDict([("ASUS", 80000), ("Toshiba", 65000),
                                           ("Dell", 90000)])
        del test_delitem_dict["Dell"]
        self.assertEquals(test_delitem_dict.__contains__("Dell"), False)
        self.assertEquals(len(test_delitem_dict), 2)

    def test_iter(self):
        keys = []
        for item_key in self.test_little_dict:
            keys.append(item_key)
        self.assertEquals(len(keys), 5)
        self.assertEquals(keys.__contains__("Lenovo"), True)
        self.assertEquals(keys.__contains__("Vaio"), True)
        self.assertEquals(keys.__contains__("Philips"), True)
        self.assertEquals(keys.__contains__("HP"), True)
        self.assertEquals(keys.__contains__("Apple"), True)


if __name__ == "__main__":
    unittest.main()
