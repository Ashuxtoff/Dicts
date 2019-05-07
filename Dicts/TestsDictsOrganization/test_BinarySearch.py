import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))
from DictsOrganizations.BinarySearch import BinarySearch


class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        self.test_common_list = ["ASUS", "Acer", "Apple", "Dell",
                                 "Samsung", "Toshiba"]

    def test_simple(self):
        self.assertEquals(BinarySearch(
            "Dell", self.test_common_list, True), 3)
        self.assertEquals(BinarySearch(
            "Toshiba", self.test_common_list, True), 5)
        self.assertEquals(BinarySearch(
            "Acer", self.test_common_list, True), 1)

    def test_None_output(self):
        self.assertEquals(BinarySearch(
            "Siemens", self.test_common_list, False), None)
        self.assertEquals(BinarySearch(
            "Lenovo", self.test_common_list, False), None)

    def test_return_index_of_absent_key(self):
        self.assertEquals(BinarySearch(
            "Lenovo", self.test_common_list, True), 4)
        self.assertEquals(BinarySearch(
            "Cronox", self.test_common_list, True), 3)


if __name__ == "__main__":
    unittest.main()
