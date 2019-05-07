import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))
from Dicts.DictsOrganizations.Tree import BinaryTree
from Dicts.DictsOrganizations.Tree import TreeNode
from Dicts.TypesDicts.TreeDict import SimpleTreeDict


class TestTreeDict(unittest.TestCase):
    def setUp(self):
        self.test_common_dict = SimpleTreeDict([("ASUS", 80000),
                                               ("Toshiba", 65000),
                                               ("Dell", 90000),
                                               ("Acer", 75000),
                                               ("Apple", 100000),
                                               ("Samsung", 60000)])
        self.test_little_dict = SimpleTreeDict([("ASUS", 80000),
                                               ("Toshiba", 65000),
                                               ("Dell", 90000)])
        self.test_empty_dict = SimpleTreeDict()

    def test_contains(self):
        self.assertEquals(self.test_common_dict.__contains__("Toshiba"), True)
        self.assertEquals(self.test_little_dict.__contains__("Apple"), False)

    def test_clear(self):
        test_clear_dict = SimpleTreeDict([("ASUS", 80000), ("Toshiba", 65000),
                                         ("Dell", 90000), ("Acer", 75000),
                                         ("Apple", 100000),
                                         ("Samsung", 60000)])
        test_clear_dict.clear()
        self.assertEquals(test_clear_dict.root, None)
        self.assertEquals(test_clear_dict.root, None)
        self.assertEquals(len(test_clear_dict), 0)

    def test_fromkeys(self):
        keys = []
        values = []
        sequence = ["1", "2", "3"]
        test_fromkeys_dict = SimpleTreeDict([("ASUS", 80000),
                                            ("Toshiba", 65000),
                                            ("Dell", 90000), ("Acer", 75000),
                                            ("Apple", 100000),
                                            ("Samsung", 60000)])
        test_fromkeys_dict.fromkeys(sequence, 1)
        for node in test_fromkeys_dict.nodes_list:
            keys.append(node.key)
            values.append(node.value)
        self.assertEquals(keys, ["1", "2", "3"])
        self.assertEquals(values, [1, 1, 1])

    def test_get(self):
        self.assertEquals(self.test_common_dict.get("ASUS"), 80000)
        self.assertEquals(self.test_little_dict.get("MSI", 45000), 45000)

    def test_items(self):
        self.assertEquals(self.test_little_dict.items(), [("ASUS", 80000),
                                                          ("Toshiba", 65000),
                                                          ("Dell", 90000)])
        self.assertEquals(self.test_empty_dict.items(), [])

    def test_keys(self):
        self.assertEquals(self.test_common_dict.keys(), ["ASUS", "Toshiba",
                                                         "Dell", "Acer",
                                                         "Apple", "Samsung"])
        self.assertEquals(self.test_empty_dict.keys(), [])

    def test_popitem(self):
        test_popitem_dict = SimpleTreeDict([("ASUS", 80000),
                                            ("Toshiba", 65000),
                                            ("Dell", 90000)])
        test_popitem_dict.popitem()
        self.assertEquals(len(test_popitem_dict), 2)
        test_popitem_dict.clear()
        with self.assertRaises(KeyError):
            test_popitem_dict.popitem()

    def test_setdefault(self):
        test_setdefault_dict = SimpleTreeDict([("ASUS", 80000),
                                              ("Toshiba", 65000),
                                              ("Dell", 90000)])
        self.assertEquals(test_setdefault_dict.setdefault("Dell"), 90000)
        self.assertEquals(len(test_setdefault_dict), 3)
        self.assertEquals(test_setdefault_dict.setdefault("MSI", 45000), 45000)
        self.assertEquals(len(test_setdefault_dict), 4)

    def test_pop(self):
        test_pop_dict = SimpleTreeDict([("ASUS", 80000), ("Toshiba", 65000),
                                       ("Dell", 90000)])
        self.assertEquals(test_pop_dict.pop("Toshiba"), 65000)
        self.assertEquals(test_pop_dict.__contains__("Toshiba"), False)
        self.assertEquals(len(test_pop_dict), 2)

    def test_values(self):
        self.assertEquals(self.test_common_dict.values(), [80000, 65000, 90000,
                                                           75000, 100000,
                                                           60000])
        self.assertEquals(self.test_empty_dict.values(), [])

    def test_update(self):
        test_update_dict = SimpleTreeDict([("ASUS", 80000), ("Toshiba", 65000),
                                          ("Dell", 90000)])
        test_update_dict.update(self.test_common_dict)
        self.assertEquals(len(test_update_dict), 6)
        for node_key in self.test_common_dict:
            self.assertEquals(test_update_dict.__contains__(node_key), True)

    def test_copy(self):
        test_copy_dict = self.test_common_dict.copy()
        self.assertEquals(len(test_copy_dict), 6)
        self.assertEquals(
            test_copy_dict.root.key, self.test_common_dict.root.key)
        self.assertEquals(
            test_copy_dict.root.value, self.test_common_dict.root.value)

    def test_eq(self):
        test_eq_dict = SimpleTreeDict([("ASUS", 80000), ("Toshiba", 65000),
                                      ("Dell", 90000), ("Acer", 75000),
                                      ("Apple", 100000), ("Samsung", 60000)])
        self.assertEquals(self.test_common_dict.__eq__(test_eq_dict), True)
        test_eq_dict = SimpleTreeDict([("ASUS", 80000), ("Toshiba", 65000),
                                      ("Dell", 90000), ("Acer", 75000),
                                      ("Apple", 100000)])
        self.assertEquals(self.test_common_dict.__eq__(test_eq_dict), False)
        test_eq_dict = SimpleTreeDict([("ASUS", 80001), ("Toshiba", 65001),
                                      ("Dell", 90001), ("Acer", 75001),
                                      ("Apple", 100001), ("Samsung", 60001)])
        self.assertEquals(self.test_common_dict.__eq__(test_eq_dict), False)
        test_eq_dict = SimpleTreeDict([("Toshiba", 65000), ("Samsung", 60000),
                                      ("Dell", 90000), ("Apple", 100000),
                                      ("Acer", 75000), ("ASUS", 80000)])
        self.assertEquals(self.test_common_dict.__eq__(test_eq_dict), False)

    def test_len(self):
        self.assertEquals(0, self.test_empty_dict.__len__())
        self.assertEquals(6, self.test_common_dict.__len__())
        self.assertEquals(3, self.test_little_dict.__len__())

    def test_delitem(self):
        test_delitem_dict = SimpleTreeDict([("ASUS", 80000),
                                            ("Toshiba", 65000),
                                            ("Dell", 90000)])
        del test_delitem_dict["Dell"]
        self.assertEquals(test_delitem_dict.__contains__("Dell"), False)
        self.assertEquals(len(test_delitem_dict), 2)

    def test_iter(self):
        keys = []
        for node_key in self.test_little_dict:
            keys.append(node_key)
        self.assertEquals(keys, ["ASUS", "Toshiba", "Dell"])


if __name__ == "__main__":
    unittest.main()
