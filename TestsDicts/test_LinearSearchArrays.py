import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))
import unittest
from Dicts.TypesDicts.LinearSearchArrays import ArraysWithLinearSearch


class TestLinearSearchArrays(unittest.TestCase):
    def setUp(self):
        self.test_common_dict = ArraysWithLinearSearch([("ASUS", 80000),
                                                        ("Toshiba", 65000),
                                                        ("Dell", 90000),
                                                        ("Acer", 75000),
                                                        ("Apple", 100000),
                                                        ("Samsung", 60000)])
        self.test_empty_dict = ArraysWithLinearSearch()
        self.test_little_dict = ArraysWithLinearSearch(
            ([("ASUS", 80000), ("Toshiba", 65000), ("Dell", 90000)]))

    def test_contains(self):
        self.assertEquals(self.test_common_dict.__contains__("Apple"), True)
        self.assertEquals(self.test_little_dict.__contains__("Apple"), False)

    def test_len(self):
        self.assertEquals(0, self.test_empty_dict.__len__())
        self.assertEquals(6, self.test_common_dict.__len__())
        self.assertEquals(3, self.test_little_dict.__len__())

    def test_eq(self):
        self.assertEquals(True, self.test_little_dict.__eq__(
            ArraysWithLinearSearch([("ASUS", 80000), ("Toshiba", 65000),
                                    ("Dell", 90000)])))
        self.assertEquals(False, self.test_common_dict.__eq__(
            self.test_little_dict))
        self.assertEquals(True, self.test_empty_dict.__eq__(
            ArraysWithLinearSearch([])))

    def test_clear(self):
        self.test_common_dict.clear()
        self.assertEquals(self.test_common_dict.keys_list, [])
        self.assertEquals(self.test_common_dict.values_list, [])

    def test_fromkeys(self):
        fromkeys_test = ArraysWithLinearSearch([])
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
        self.assertEquals(result, [("ASUS", 80000), ("Toshiba", 65000),
                                   ("Dell", 90000)])

    def test_keys(self):
        result = self.test_common_dict.keys()
        self.assertEquals(result, ["ASUS", "Toshiba", "Dell", "Acer",
                                   "Apple", "Samsung"])

    def test_setdefault(self):
        self.assertEquals(65000, self.test_common_dict.setdefault("Toshiba"))
        self.assertEquals(45000, self.test_empty_dict.setdefault("MIO", 45000))
        self.test_empty_dict.clear()

    def test_pop(self):
        pop_test = ArraysWithLinearSearch(
            [("Toyota", 1937), ("Nissan", 1933), ("Suzuki", 1909),
             ("Honda", 1948), ("Subaru", 1953)])
        self.assertEquals(1933, pop_test.pop("Nissan"))
        self.assertEquals(4, len(pop_test))
        self.assertEquals(0, pop_test.pop("KIA", 0))
        # with self.assertRaises(KeyError):
        #     pop_test.pop(None)

    def test_popitem(self):
        popitem_test = ArraysWithLinearSearch(
            [("Toyota", 1937), ("Nissan", 1933), ("Suzuki", 1909),
             ("Honda", 1948), ("Subaru", 1953)])
        popitem_test.popitem()
        self.assertEquals(4, len(popitem_test))

    def test_values(self):
        self.assertEquals([80000, 65000, 90000, 75000, 100000, 60000],
                          self.test_common_dict.values())

    def test_copy(self):
        self.assertEquals(ArraysWithLinearSearch(
            [("ASUS", 80000), ("Toshiba", 65000), ("Dell", 90000)]),
            self.test_little_dict.copy())
        self. assertEquals(ArraysWithLinearSearch([]),
                           self.test_empty_dict.copy())

    def test_delitem(self):
        delitem_test = ArraysWithLinearSearch(
            [("Toyota", 1937), ("Nissan", 1933), ("Suzuki", 1909),
             ("Honda", 1948)])
        del delitem_test["Toyota"]
        self.assertEquals(ArraysWithLinearSearch(
            [("Nissan", 1933), ("Suzuki", 1909), ("Honda", 1948)]).keys(),
            delitem_test.keys())
        self.assertEquals(ArraysWithLinearSearch(
            [("Nissan", 1933), ("Suzuki", 1909), ("Honda", 1948)]).values(),
            delitem_test.values())

    def test_update(self):
        update_test = ArraysWithLinearSearch(
            [("Toyota", 1937), ("Nissan", 1933)])
        help_update_test = ArraysWithLinearSearch(
            [("Suzuki", 1909), ("Honda", 1948)])
        update_test.update(help_update_test)
        self.assertEquals(ArraysWithLinearSearch(
            [("Toyota", 1937), ("Nissan", 1933), ("Suzuki", 1909),
             ("Honda", 1948)]),
            update_test)

    def test_iter(self):
        iter_test = ArraysWithLinearSearch(
            [("Toyota", 1937), ("Nissan", 1933), ("Suzuki", 1909),
             ("Honda", 1948), ("Subaru", 1953)])
        keys = []
        for element in iter_test:
            keys.append(element)
        self.assertEquals(keys, ["Toyota", "Nissan", "Suzuki",
                                 "Honda", "Subaru"])


if __name__ == "__main__":
    unittest.main()
