import random
import string
import sys
import os
import itertools
from queue import Queue
from timeit import default_timer as timer
from pympler import asizeof
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))
from Dicts.DictsOrganizations.Tree import TreeNode
from Dicts.TypesDicts.BalancedTreeDict import AVLTreeDict
from Dicts.TypesDicts.HashTableDict import HashTableDict
from Dicts.TypesDicts.LinearSearchArrays import ArraysWithLinearSearch
from Dicts.TypesDicts.SortedBinarySearchArrays import BinarySearchArrays
from Dicts.TypesDicts.TreeDict import SimpleTreeDict


class DictsTester():
    def __init__(self, tested_dict, random_data, increase_data):
        self.tested_class = tested_dict
        self.random_data = random_data
        self.increase_data = increase_data
        self.random_dict = tested_dict(random_data)
        self.increase_dict = tested_dict(increase_data)
        self.increase_dict_copy = self.increase_dict.copy()
        self.random_dict_copy = self.random_dict.copy()

    def measure_time(self, function, *args):
        start_time = timer()
        function(*args)
        finish_time = timer()
        return finish_time - start_time

    def key_generating(self):
        key = ''.join(random.choice(string.ascii_letters + string.digits)
                      for i in range(len(self.random_data[0][0])))
        return key

    def pairs_generating(self, dictionary, mode):
        tuples = []

        def random_keys_pairs_generating():
            tuples.clear()
            while len(tuples) < len(self.random_dict):
                key = self.key_generating()
                value = random.randint(1, 10000)
                tuples.append((key, value))

        def coincidence_keys_pairs_generating():
            tuples.clear()
            keys = list(dictionary.keys())
            while len(tuples) < len(self.random_dict):
                value = random.randint(1, 10000)
                tuples.append((keys[len(tuples)], value))

        def exceptional_keys_pairs_generating():
            tuples.clear()
            while len(tuples) < len(self.random_dict):
                key = self.key_generating()
                if not dictionary.__contains__(key):
                    value = random.randint(1, 10000)
                    tuples.append((key, value))

        funcs_dict = {"random": random_keys_pairs_generating,
                      "coincidence": coincidence_keys_pairs_generating,
                      "exceptional": exceptional_keys_pairs_generating
                      }
        funcs_dict[mode]()
        return tuples

    def exceptional_key_generating(self, needed_dict=None):
        key = self.key_generating()
        while needed_dict.__contains__(key):
            key = self.key_generating()
        return key

    def iterating(self, dictionary):
        for element in dictionary:
            a = element

    def translate_balanced_tree_to_simple(self, balanced_tree):
        tree = SimpleTreeDict()

        def translate_nodes(node):
            if node is not None:
                tree.add_node(TreeNode(node.key, node.value))
                translate_nodes(node.left)
                translate_nodes(node.right)

        translate_nodes(balanced_tree.root)
        return tree

    def make_special_nodes_list(self, balanced_tree):
        nodes_list = []
        queue = Queue()
        queue.put(balanced_tree.root)
        while queue.qsize() > 0:
            node = queue.get()
            nodes_list.append(node.key)
            if node.left is not None:
                queue.put(node.left)
            if node.right is not None:
                queue.put(node.right)
        return nodes_list

    def reestablish_dicts_copies(self, *dicts):
        if dicts.__contains__(self.random_dict_copy):
            self.random_dict_copy = self.random_dict.copy()
        if self.tested_class is not dict and dicts.__contains__(
                self.increase_dict_copy):
            self.increase_dict_copy = self.increase_dict.copy()
        if len(dicts) == 0:
            self.random_dict_copy = self.random_dict.copy()
            self.increase_dict_copy = self.increase_dict.copy()

    def take_random_key(self, dict):
        return random.choice(list(dict.keys()))

    def make_specific_hash_keys(self, needed_hash, count, size_height=10):
        sequence = []
        while len(sequence) < count:
            key = self.key_generating()
            if hash(key) % size_height == needed_hash:
                sequence.append(key)
        return sequence

    def make_all_collisions_hash_table(self, needed_hash, count,
                                       keys_values=10):
        elements_tuples = []
        one_hash_keys = self.make_specific_hash_keys(needed_hash, count)
        for key in one_hash_keys:
            elements_tuples.append((key, keys_values))
        exceptional_hash_table = HashTableDict(elements_tuples)
        return exceptional_hash_table

    def extreme_cases_contains_testing(self):
        if self.tested_class is ArraysWithLinearSearch:
            key_longest = self.random_dict.keys_list[len(self.random_dict) - 1]
            key_shortest = self.random_dict.keys_list[0]
        if self.tested_class is BinarySearchArrays:
            key_longest = self.exceptional_key_generating(self.random_dict)
            key_shortest = self.random_dict.keys()[0]
        if self.tested_class is SimpleTreeDict:
            key_longest = self.increase_dict.keys()[
                          len(self.increase_dict) - 1]
            key_shortest = self.increase_dict.root.key
        if self.tested_class is AVLTreeDict:
            key_longest = self.exceptional_key_generating(self.random_dict)
            key_shortest = self.random_dict.root.key
        if self.tested_class is HashTableDict:
            longest_collisions_nubmer = self.random_dict.get_longest_collision
            keys = self.random_dict.keys()[::-1]
            key_longest = ""
            for element in keys:
                if self.random_dict.get_hash(
                        element) == longest_collisions_nubmer:
                    key_longest = element
            key_shortest = self.random_dict.hash_table[0][1]
        if self.tested_class is SimpleTreeDict:
            longest_time = self.measure_time(self.increase_dict.__contains__,
                                             key_longest)
            shortest_time = self.measure_time(self.increase_dict.__contains__,
                                              key_shortest)
            return (longest_time, shortest_time)
        longest_time = self.measure_time(self.random_dict.__contains__,
                                         key_longest)
        shortest_time = self.measure_time(self.random_dict.__contains__,
                                          key_shortest)
        return (shortest_time, longest_time)

    def extreme_cases_fromkeys_testing(self):
        if self.tested_class is ArraysWithLinearSearch:
            sequence_shortest = sequence_longest = self.random_data
        if self.tested_class is BinarySearchArrays:
            sequence_longest = self.increase_data[::-1]
            sequence_shortest = self.increase_data
        if self.tested_class is SimpleTreeDict:
            sequence_longest = self.increase_dict.keys()
            help_balansed_tree = AVLTreeDict(self.random_data)
            sequence_shortest = self.make_special_nodes_list(
                help_balansed_tree)
        if self.tested_class is AVLTreeDict:
            sequence_longest = self.increase_data
            sequence_shortest = self.make_special_nodes_list(
                AVLTreeDict(self.random_data))
        if self.tested_class is HashTableDict:
            sequence_longest = self.make_specific_hash_keys(
                1, len(self.random_data))
            sequence = []
            subsequences = []
            for i in range(self.random_dict.size_height):
                subsequence = self.make_specific_hash_keys(
                    i, len(self.random_dict)//self.random_dict.size_height)
                subsequences.append(subsequence)
            for subsequence in subsequences:
                sequence = list(set(sequence + subsequence))
            sequence_shortest = sequence
        if self.tested_class is SimpleTreeDict:
            longest_time = self.measure_time(self.increase_dict_copy.fromkeys,
                                             sequence_longest, 10)
            shortest_time = self.measure_time(self.random_dict_copy.fromkeys,
                                              sequence_shortest, 10)
            self.reestablish_dicts_copies(self.random_dict_copy,
                                          self.increase_dict_copy)
            return (shortest_time, longest_time)
        longest_time = self.measure_time(self.random_dict_copy.fromkeys,
                                         sequence_longest, 10)
        shortest_time = self.measure_time(self.random_dict_copy.fromkeys,
                                          sequence_shortest, 10)
        self.reestablish_dicts_copies(self.random_dict_copy)
        return (shortest_time, longest_time)

    def extreme_cases_get_testing(self):
        longest_time = 0
        shortest_time = 0
        if self.tested_class is ArraysWithLinearSearch:
            key_longest = self.random_dict.keys()[-1]
            key_shortest = self.random_dict.keys()[0]
        if self.tested_class is BinarySearchArrays:
            key_longest = self.exceptional_key_generating(self.random_dict)
            key_shortest = self.random_dict.keys()[
                (len(self.random_dict)-1)//2]
        if self.tested_class is SimpleTreeDict:
            key_longest = self.increase_data[-1][0]
            key_shortest = self.random_dict.root.key
        if self.tested_class is AVLTreeDict:
            key_longest = self.exceptional_key_generating(self.random_dict)
            key_shortest = self.random_dict.root.key
        if self.tested_class is HashTableDict:
            key_longest = self.exceptional_key_generating(self.random_dict)
            key_shortest = self.random_dict.hash_table[0][1]
        if self.tested_class is SimpleTreeDict:
            longest_time = self.measure_time(self.increase_dict.get,
                                             key_longest)
            shortest_time = self.measure_time(self.random_dict.get,
                                              key_shortest)
            return (shortest_time, longest_time)
        longest_time = self.measure_time(self.random_dict.get, key_longest, 10)
        shortest_time = self.measure_time(self.random_dict.get,
                                          key_shortest, 10)
        return (shortest_time, longest_time)

    def extreme_cases_setdefault_testing(self):
        if self.tested_class is ArraysWithLinearSearch:
            key_longest = self.exceptional_key_generating(self.random_dict)
            key_shortest = self.random_dict.keys_list[0]
        if self.tested_class is BinarySearchArrays:
            key_longest = self.exceptional_key_generating(self.random_dict)
            key_shortest = self.random_dict.keys()[
                (len(self.random_dict)-1)//2]
        if self.tested_class is SimpleTreeDict:
            key_longest = self.increase_data[-1][0]
            key_shortest = self.random_dict.root.key
            longest_time = self.measure_time(self.increase_dict.setdefault,
                                             key_longest)
            shortest_time = self.measure_time(self.random_dict.setdefault,
                                              key_shortest)
        if self.tested_class is AVLTreeDict:
            key_longest = self.exceptional_key_generating(self.random_dict)
            key_shortest = self.random_dict.root.key
        if self.tested_class is HashTableDict:
            equals_hash_keys_hash_table = self.make_all_collisions_hash_table(
                1, len(self.random_data))
            key_longest = self.make_specific_hash_keys(1, 1)[0]
            while equals_hash_keys_hash_table.keys().__contains__(key_longest):
                key_longest = self.make_specific_hash_keys(1, 1)[0]
            key_shortest = self.random_dict.hash_table[0][1].key
            longest_time = self.measure_time(
                equals_hash_keys_hash_table.setdefault, key_longest, 10)
            shortest_time = self.measure_time(self.random_dict_copy.setdefault,
                                              key_shortest)
        longest_time = self.measure_time(self.random_dict_copy.setdefault,
                                         key_longest, 10)
        shortest_time = self.measure_time(self.random_dict_copy.setdefault,
                                          key_shortest, 10)
        self.reestablish_dicts_copies(self.random_dict_copy)
        return (shortest_time, longest_time)

    def extreme_cases_pop_testimg(self):
        if self.tested_class is ArraysWithLinearSearch:
            key_longest = self.random_dict.keys_list[-1]
            key_shortest = self.random_dict.keys_list[0]
        if self.tested_class is BinarySearchArrays:
            key_longest = self.random_dict.keys()[1]
            key_shortest = self.random_dict.keys()[
                (len(self.random_dict)-1)//2]
        if self.tested_class is SimpleTreeDict:
            key_longest = self.increase_data[-1][0]
            key_shortest = self.random_data[0][0]
            longest_time = self.measure_time(self.increase_dict.pop,
                                             key_longest)
            shortest_time = self.measure_time(self.increase_dict.pop,
                                              key_shortest)
        if self.tested_class is AVLTreeDict:
            key_longest = max(self.random_dict.keys())
            key_shortest = self.random_dict.root.key
        if self.tested_class is HashTableDict:
            equals_hash_keys_hash_table = self.make_all_collisions_hash_table(
                1, 1000)
            key_longest = equals_hash_keys_hash_table.hash_table[1][1000]
            key_shortest = self.random_dict.hash_table[0][1]
            longest_time = self.measure_time(equals_hash_keys_hash_table.pop,
                                             key_longest)
            shortest_time = self.measure_time(self.random_dict.pop,
                                              key_shortest)
        longest_time = self.measure_time(self.random_dict.pop, key_longest)
        shortest_time = self.measure_time(self.random_dict.pop, key_shortest)
        return (shortest_time, longest_time)

    def extreme_cases_update_testing(self):
        if self.tested_class is ArraysWithLinearSearch:
            dict_longest = self.random_dict_copy
            dict_shortest = ArraysWithLinearSearch(
                self.pairs_generating(self.random_dict, "exceptional"))
        if self.tested_class is BinarySearchArrays:
            dict_longest = BinarySearchArrays(
                self.pairs_generating(self.random_dict, "exceptional"))
            dict_shortest = self.random_dict_copy
        if self.tested_class is SimpleTreeDict:
            dict_longest = SimpleTreeDict(
                self.pairs_generating(self.increase_dict, "exceptional"))
            dict_shortest = self.translate_balanced_tree_to_simple(
                AVLTreeDict(self.pairs_generating(self.random_dict,
                            "coincidence")))
            longest_time = self.measure_time(self.increase_dict_copy.update,
                                             dict_longest)
            self.reestablish_dicts_copies(self.increase_dict_copy)
            shortest_time = self.measure_time(self.increase_dict_copy.update,
                                              dict_shortest)
            self.reestablish_dicts_copies(self.increase_dict_copy)
            return (shortest_time, longest_time)
        if self.tested_class is AVLTreeDict:
            dict_longest = AVLTreeDict(self.pairs_generating(self.random_dict,
                                       "coincidence"))
            dict_shortest = AVLTreeDict(self.pairs_generating(self.random_dict,
                                        "exceptional"))
        if self.tested_class is HashTableDict:
            dict_longest = HashTableDict(
                self.pairs_generating(self.random_dict, "exceptional"))
            dict_shortest = HashTableDict(
                self.pairs_generating(self.random_dict, "coincidence"))
        longest_time = self.measure_time(self.random_dict_copy.update,
                                         dict_longest)
        self.reestablish_dicts_copies()
        shortest_time = self.measure_time(
            self.random_dict_copy.update, dict_shortest)
        return (shortest_time, longest_time)

    def common_contains_testing(self):
        key = self.key_generating()
        result_time = self.measure_time(self.random_dict.__contains__, key)
        return result_time

    def common_clear_testing(self):
        help_dict = self.random_dict.copy()
        result_time = self.measure_time(help_dict.clear)
        return result_time

    def common_fromkeys_testing(self):
        value = random.randint(0, 1000)
        random_keys = self.random_dict.keys()
        result_time = self.measure_time(
            self.random_dict_copy.fromkeys, random_keys, value)
        self.reestablish_dicts_copies(self.random_dict_copy)
        return result_time

    def common_get_testing(self):
        key = self.key_generating()
        result_time = self.measure_time(self.random_dict.get, key, 0)
        return result_time

    def common_items_testing(self):
        result_time = self.measure_time(self.random_dict.items)
        return result_time

    def common_keys_testing(self):
        result_time = self.measure_time(self.random_dict.keys)
        return result_time

    def common_popitem_testing(self):
        result_time = self.measure_time(self.random_dict_copy.popitem)
        self.reestablish_dicts_copies(self.random_dict_copy)
        return result_time

    def common_setdefault_testing(self):
        key = self.take_random_key(self.random_dict)
        result = self.measure_time(
            self.random_dict_copy.setdefault, key)
        self.reestablish_dicts_copies(self.random_dict_copy)
        return result

    def common_pop_testing(self):
        key = self.take_random_key(self.random_dict)
        attend_result_time = self.measure_time(
            self.random_dict_copy.pop, key)
        self.reestablish_dicts_copies(self.random_dict_copy)
        return attend_result_time

    def common_values_testing(self):
        result_time = self.measure_time(self.random_dict.values)
        return result_time

    def common_update_testing(self):
        result_time = self.measure_time(
            self.random_dict_copy.update, self.tested_class(
                self.pairs_generating(self.random_dict, "random")))
        return result_time

    def common_copy_testing(self):
        result_time = self.measure_time(self.random_dict.copy)
        return result_time

    def test_common_funcs(self):
        return {"clear": self.common_clear_testing(),
                "contains": self.common_contains_testing(),
                "fromkeys": self.common_fromkeys_testing(),
                "copy": self.common_copy_testing(),
                "get": self.common_get_testing(),
                "items": self.common_items_testing(),
                "keys": self.common_keys_testing(),
                "pop": self.common_pop_testing(),
                "popitem": self.common_popitem_testing(),
                "setdefault": self.common_setdefault_testing(),
                "update": self.common_update_testing(),
                "values": self.common_values_testing()}

    def test_extreme_funcs(self, mode):
        if mode == 'best':
            i = 0
        if mode == 'worst':
            i = 1
        return {"contains": self.extreme_cases_contains_testing()[i],
                "fromkeys": self.extreme_cases_fromkeys_testing()[i],
                "get": self.extreme_cases_get_testing()[i],
                "pop": self.extreme_cases_pop_testimg()[i],
                "setdefault": self.extreme_cases_setdefault_testing()[i],
                "update": self.extreme_cases_update_testing()[i]}

    def test_memory(self):
        lin = ArraysWithLinearSearch(self.random_data)
        bin = BinarySearchArrays(self.random_data)
        tree = SimpleTreeDict(self.random_data)
        avl = AVLTreeDict(self.random_data)
        hash = HashTableDict(self.random_data)
        result_dict = {ArraysWithLinearSearch: asizeof.asizeof(lin),
                       BinarySearchArrays: asizeof.asizeof(bin),
                       SimpleTreeDict: asizeof.asizeof(tree),
                       AVLTreeDict: asizeof.asizeof(avl),
                       HashTableDict: asizeof.asizeof(hash)}
        return result_dict
