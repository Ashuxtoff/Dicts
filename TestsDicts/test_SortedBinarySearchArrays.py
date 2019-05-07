import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))
from Dicts.TypesDicts.SortedBinarySearchArrays import BinarySearchArrays


class TestBinarySearchArrays(unittest.TestCase):
    def setUp(self):
        self.test_common_dict = BinarySearchArrays(
            [("ASUS", 80000), ("Acer", 75000), ("Apple", 100000),
             ("Dell", 90000), ("Samsung", 60000), ("Toshiba", 65000)]
        )
        self.test_empty_dict = BinarySearchArrays()
        self.test_little_dict = BinarySearchArrays(
            [("ASUS", 80000), ("Dell", 90000), ("Toshiba", 65000)]
        )

    def test_contains(self):
        self.assertEquals(self.test_common_dict.__contains__("Apple"), True)
        self.assertEquals(self.test_little_dict.__contains__("Apple"), False)

    def test_len(self):
        self.assertEquals(0, self.test_empty_dict.__len__())
        self.assertEquals(6, self.test_common_dict.__len__())
        self.assertEquals(3, self.test_little_dict.__len__())

    def test_eq(self):
        self.assertEquals(True, self.test_little_dict.__eq__(
            BinarySearchArrays([("ASUS", 80000), ("Dell", 90000),
                                ("Toshiba", 65000)])))
        self.assertEquals(False, self.test_common_dict.__eq__(
            self.test_little_dict))
        self.assertEquals(True, self.test_empty_dict.__eq__(
            BinarySearchArrays([])))

    def test_clear(self):
        self.test_common_dict.clear()
        self.assertEquals(self.test_common_dict.keys_list, [])
        self.assertEquals(self.test_common_dict.values_list, [])

    def test_fromkeys(self):
        fromkeys_test = BinarySearchArrays([])
        fromkeys_test.fromkeys(["a", "b", "c"])
        self.assertEquals(fromkeys_test.keys_list, ["a", "b", "c"])
        self.assertEquals(fromkeys_test.values_list, [None, None, None])
        fromkeys_test.fromkeys(["d", "e", "f"], 1)
        self.assertEquals(fromkeys_test.keys_list, ["d", "e", "f"])
        self.assertEquals(fromkeys_test.values_list, [1, 1, 1])

    def test_get(self):
        result = self.test_common_dict.get("ASUS")
        self.assertEquals(result, 80000)
        result = self.test_common_dict.get("Siemens")
        self.assertEquals(result, None)
        result = self.test_common_dict.get("Siemens", 50000)
        self.assertEquals(result, 50000)

    def test_items(self):
        result = self.test_little_dict.items()
        self.assertEquals(result, [("ASUS", 80000), ("Dell", 90000),
                                   ("Toshiba", 65000)])

    def test_keys(self):
        result = self.test_common_dict.keys()
        self.assertEquals(result, ["ASUS", "Acer", "Apple",
                                   "Dell", "Samsung", "Toshiba"])

    def test_setdefault(self):
        self.assertEquals(65000, self.test_common_dict.setdefault("Toshiba"))
        self.assertEquals(45000, self.test_empty_dict.setdefault("MIO", 45000))
        self.test_empty_dict.clear()

    def test_pop(self):
        pop_test = BinarySearchArrays(
            [("Honda", 1948), ("Nissan", 1933), ("Subaru", 1953),
             ("Suzuki", 1909), ("Toyota", 1937)])
        self.assertEquals(1933, pop_test.pop("Nissan"))
        self.assertEquals(4, len(pop_test))
        self.assertEquals(0, pop_test.pop("KIA", 0))
        # with self.assertRaises(KeyError):
        #     pop_test.pop(None)

    def test_popitem(self):
        popitem_test = BinarySearchArrays(
            [("Honda", 1948), ("Nissan", 1933), ("Subaru", 1953),
             ("Suzuki", 1909), ("Toyota", 1937)])
        popitem_test.popitem()
        self.assertEquals(4, len(popitem_test))
        with self.assertRaises(KeyError):
            self.test_empty_dict.popitem()

    def test_values(self):
        self.assertEquals([80000, 75000, 100000, 90000, 60000, 65000],
                          self.test_common_dict.values())

    def test_copy(self):
        self.assertEquals(BinarySearchArrays(
            [("ASUS", 80000), ("Dell", 90000), ("Toshiba", 65000)]).keys(),
            self.test_little_dict.copy().keys())
        self.assertEquals(BinarySearchArrays(
            [("ASUS", 80000), ("Dell", 90000), ("Toshiba", 65000)]).values(),
            self.test_little_dict.copy().values())
        self. assertEquals(BinarySearchArrays([]),
                           self.test_empty_dict.copy())

    def test_delitem(self):
        delitem_test = BinarySearchArrays(
            [("Honda", 1948), ("Nissan", 1933), ("Suzuki", 1909),
             ("Toyota", 1937)])
        del delitem_test["Honda"]
        self.assertEquals(BinarySearchArrays(
            [("Nissan", 1933), ("Suzuki", 1909), ("Toyota", 1937)]).keys(),
            delitem_test.keys())
        self.assertEquals(BinarySearchArrays(
            [("Nissan", 1933), ("Suzuki", 1909), ("Toyota", 1937)]).values(),
            delitem_test.values())

    def test_iter(self):
        keys = []
        for key in self.test_common_dict.keys_list:
            keys.append(key)
        self.assertEquals(keys, ["ASUS", "Acer", "Apple",
                                 "Dell", "Samsung", "Toshiba"])

    def test_update(self):
        update_test = BinarySearchArrays(
            [("Nissan", 1933), ("Toyota", 1937)])
        help_update_test = BinarySearchArrays(
            [("Honda", 1948), ("Suzuki", 1909)])
        update_test.update(help_update_test)
        self.assertEquals(BinarySearchArrays(
            [("Honda", 1948), ("Nissan", 1933), ("Suzuki", 1909),
             ("Toyota", 1937)]),
            update_test)


if __name__ == "__main__":
    unittest.main()
