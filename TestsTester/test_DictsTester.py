import unittest
import sys
import os
import random
import string
import inspect
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))
from Tester.DictsTester import DictsTester
from Tester.Measurer import Measurer
from Dicts.TypesDicts.BalancedTreeDict import AVLTreeDict
from Dicts.TypesDicts.HashTableDict import HashTableDict
from Dicts.TypesDicts.TreeDict import SimpleTreeDict


class TestDictsTester(unittest.TestCase):
    def setUp(self):
        length = 100
        self.measurer = Measurer(length)
        self.random_data = self.measurer.make_input_random_data(length)
        self.increase_data = self.measurer.make_input_increase_data(length)
        self.random_tree_dict = HashTableDict(self.random_data)
        self.increase_tree_dict = HashTableDict(self.increase_data)
        self.tester = DictsTester(HashTableDict, self.random_data,
                                  self.increase_data)
        self.common_tests_list = [self.tester.common_contains_testing,
                                  self.tester.common_fromkeys_testing,
                                  self.tester.common_get_testing,
                                  self.tester.common_pop_testing,
                                  self.tester.common_setdefault_testing,
                                  self.tester.common_update_testing,
                                  self.tester.common_clear_testing,
                                  self.tester.common_copy_testing,
                                  self.tester.common_items_testing,
                                  self.tester.common_keys_testing,
                                  self.tester.common_popitem_testing
                                  ]
        self.extreme_cases_tests_list = [
            self.tester.extreme_cases_contains_testing,
            self.tester.extreme_cases_fromkeys_testing,
            self.tester.extreme_cases_get_testing,
            self.tester.extreme_cases_pop_testimg,
            self.tester.extreme_cases_setdefault_testing,
            self.tester.extreme_cases_update_testing
        ]

    def test_measure_time(self):
        key = ''.join(random.choice(string.ascii_letters + string.digits)
                      for i in range(len(self.random_data[0][0])))
        result_time = self.tester.measure_time(
            self.random_tree_dict.__contains__, key)
        self.assertGreater(str(result_time), "0")

    def test_key_generating(self):
        key = self.tester.key_generating()
        self.assertEquals(len(self.random_data[0][0]), len(key))

    def test_pairs_generating(self):
        random_keys_tuples = self.tester.pairs_generating(
            self.random_tree_dict, "random")
        coincidence_keys_tuples = self.tester.pairs_generating(
            self.random_tree_dict, "coincidence")
        exceptional_keys_tuples = self.tester.pairs_generating(
            self.random_tree_dict, "exceptional")
        random_keys = {tuple_key[0] for tuple_key in random_keys_tuples}
        coincidence_keys = {tuple_key[0]
                            for tuple_key in coincidence_keys_tuples}
        exceptional_keys = {tuple_key[0]
                            for tuple_key in exceptional_keys_tuples}
        keys = self.random_tree_dict.keys()
        self.assertFalse(set(keys).intersection(random_keys) == random_keys)
        self.assertEquals(set(keys).intersection(coincidence_keys),
                          coincidence_keys)
        self.assertEquals(len(set(keys).intersection(exceptional_keys)), 0)

    def test_exceptional_key_generating(self):
        key = self.tester.exceptional_key_generating(self.tester.random_dict)
        self.assertNotEquals(key, None)
        self.assertFalse(self.tester.random_dict.__contains__(key))

    def test_reestablish_dict_copies(self):
        self.tester.random_dict_copy.update(self.tester.increase_dict)
        self.tester.reestablish_dicts_copies()
        self.assertEquals(self.tester.random_dict,
                          self.tester.random_dict_copy)
        self.assertEquals(self.tester.increase_dict,
                          self.tester.increase_dict_copy)

    def test_take_random_keys(self):
        key = self.tester.take_random_key(self.tester.random_dict)
        self.assertIn(key, list(self.tester.random_dict.keys()))

    def test_translate_balanced_tree_to_simple(self):
        balanced_tree = AVLTreeDict(self.random_data)
        simple_tree = self.tester.translate_balanced_tree_to_simple(
            balanced_tree)
        self.assertEquals(balanced_tree.root.key, simple_tree.root.key)
        self.assertEquals(balanced_tree.root.left.key,
                          simple_tree.root.left.key)
        self.assertEquals(balanced_tree.root.left.left.right.right.left.key,
                          simple_tree.root.left.left.right.right.left.key)

    def test_make_special_nodes_list(self):
        balanced_tree = AVLTreeDict(self.random_data)
        keys = self.tester.make_special_nodes_list(balanced_tree)
        input_tuple = [(x, 10) for x in keys]
        tree_dict = SimpleTreeDict(input_tuple)
        self.assertEquals(balanced_tree.root.key, tree_dict.root.key)
        self.assertEquals(balanced_tree.root.right.left.key,
                          tree_dict.root.right.left.key)
        self.assertEquals(balanced_tree.root.left.right.right.left.key,
                          tree_dict.root.left.right.right.left.key)

    def test_make_specific_hash_keys(self):
        keys = self.tester.make_specific_hash_keys(1, 20)
        for key in keys:
            self.assertEquals(hash(key) % 10, 1)

    def test_make_all_collisions_hash_table(self):
        exceptional_dict = self.tester.make_all_collisions_hash_table(1, 20)
        for key in exceptional_dict:
            self.assertEquals(1, hash(key) % 10)

    def test_tests_working(self):
        for common_test in self.common_tests_list:
            result = common_test()
            if type(result) is float:
                self.assertGreater(result, 0.0)
            else:
                for result_part in result:
                    self.assertGreater(result_part, 0.0)
        for extreme_test in self.extreme_cases_tests_list:
            result = extreme_test()
            for result_part in result:
                self.assertGreater(result_part, 0.0)

    def test_memory_testing(self):
        res = self.tester.test_memory()
        for key in res:
            self.assertEqual(type(res[key]), int)


if __name__ == "__main__":
    unittest.main()
