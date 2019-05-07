import copy
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))
import random
from DictsOrganizations.Tree import BinaryTree
from DictsOrganizations.Tree import TreeNode
from DictsOrganizations.DictBase import DictBase


class SimpleTreeDict(BinaryTree, DictBase):
    def __init__(self, tuples_list=[]):
        super().__init__()
        for node_tuple in tuples_list:
            self.add_node(TreeNode(node_tuple[0], node_tuple[1]))

    def __getitem__(self, key):
        node = self.search(self.root, key)
        if node is None:
            return None
        return node.value

    def __contains__(self, needed_key):  # поиск самого большого/маленького,
        if self.search(self.root, needed_key) is None:  # ключи отсортированы
            return False
        return True

    def clear(self):
        self.nodes_list.clear()
        self.root = None

    def fromkeys(self, sequence, value=None):  # sequence возрастающая/убывающа
        self.clear()  # и отсортированный селф
        for i in range(len(sequence)):
            new_node = TreeNode(sequence[i], value)
            self.add_node(new_node)

    def get(self, needed_key, default=None):
        if self.search(self.root, needed_key) is None:
            return default
        else:  # сложный случай самого большого/маленького отсротированный селф
            return self.search(self.root, needed_key).value

    def items(self):
        pairs = []
        for node in self.nodes_list:
            pairs.append((node.key, node.value))
        return pairs

    def keys(self):
        keys = []
        for node in self.nodes_list:
            keys.append(node.key)
        return keys

    def popitem(self):
        if len(self) == 0:
            raise KeyError
        random_node = self.nodes_list[random.randint(0, len(self)-1)]
        self.remove(random_node)
        return (random_node.key, random_node.value)

    def setdefault(self, needed_key, value=None):  # поиск наибольшего
        if self.search(self.root, needed_key) is None:  # осортированный селф
            self.add_node(TreeNode(needed_key, value))
        return self.search(self.root, needed_key).value

    def pop(self, needed_key, default=None):
        if needed_key is None:
            # raise KeyError
            return None
        needed_node = self.search(self.root, needed_key)
        if needed_node is None:
            return default  # самого большого или самого маленького
        needed_value = needed_node.value   # отсортированный селф
        self.remove(needed_node)
        return needed_value

    def values(self):
        values = []
        for node in self.nodes_list:
            values.append(node.value)
        return values

    def update(self, other):  # различные other и self, оба отсортированы
        for node in other.nodes_list:
            if self.search(self.root, node.key) is None:
                self.add_node(TreeNode(node.key, node.value))
            else:
                old_node = self.search(self.root, node.key)
                old_node.value = node.value
        return None

    def copy(self):
        new_list_node = []
        for node in self.nodes_list:
            new_node = (node.key, node.value)
            new_list_node.append(new_node)
        new_dict = SimpleTreeDict(new_list_node)
        return new_dict

    def __eq__(self, other):  # равные деревья
        if len(self.nodes_list) != len(other.nodes_list):
            return False
        for i in range(0, len(self.nodes_list)):
            searched = self.search(self.root, other.nodes_list[i].key)
            if searched is None:
                return False
            other_node = other.nodes_list[i]
            if (other_node.parent is not None and searched.parent is not None
                and other_node.parent.key != searched.parent.key
                and other_node.parent.value != searched.parent.value) \
                or (other_node.left is not None and searched.left is not None
                    and (other_node.left.key != searched.left.key
                         or other_node.left.value != searched.left.value)) \
                or (other_node.right is not None and searched.right is not None
                    and (other_node.right.key != searched.right.key
                         or other_node.right.value != searched.right.value)):
                return False
        return True

    def __len__(self):
        return len(self.nodes_list)

    def __delitem__(self, key):
        search_result = self.search(self.root, key)
        if search_result is None:
            raise KeyError
        self.remove(search_result)
        del search_result

    def __iter__(self):
        return self.keys().__iter__()
