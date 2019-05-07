import copy
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))
import random
from DictsOrganizations.BalancedTree import AVLTree
from DictsOrganizations.BalancedTree import BalancedTreeNode
from DictsOrganizations.DictBase import DictBase


class AVLTreeDict(AVLTree, DictBase):
    def __init__(self, tuple_list=None):
        super().__init__()
        if tuple_list is not None:
            for node in tuple_list:
                self.add_node(BalancedTreeNode(self.root, node[0], node[1]))

    def __getitem__(self, key):
        node = self.search(key)
        if node is None:
            return None
        return node.value

    def __contains__(self, needed_key):  # самый сложный - ключа нет
        if self.search(needed_key) is None:
            return False
        return True

    def clear(self):  # не имеет значения (пропорционально кол-ву эл-тов)
        self.nodes_list.clear()
        self.root = None

    def fromkeys(self, sequence, value=None):  # возрастающая sequence
        self.clear()
        for i in range(len(sequence)):
            new_node = BalancedTreeNode(self.root, sequence[i], value)
            self.add_node(new_node)

    def get(self, needed_key, default=None):  # самый сложный - ключа нет
        if self.search(needed_key) is None:
            return default
        else:
            return self.search(needed_key).value

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

    def popitem(self):  # метод рандомизирован
        if len(self.nodes_list) == 0:
            raise KeyError
        random_node = self.nodes_list[
            random.randint(0, len(self.nodes_list)-1)]
        self.remove(random_node.key)
        return (random_node.key, random_node.value)

    def setdefault(self, needed_key, value=None):  # самый сложный - ключа нет
        if self.search(needed_key) is None:
            self.add_node(BalancedTreeNode(self.root, needed_key, value))
        return self.search(needed_key).value

    def pop(self, needed_key, default=None):  # самый сложный - самый большой
        if needed_key is None:
            # raise KeyError
            return None
        needed_node = self.search(needed_key)
        if needed_node is None:
            return default
        needed_value = needed_node.value
        self.remove(needed_node.key)
        return needed_value

    def values(self):
        values = []
        for node in self.nodes_list:
            values.append(node.value)
        return values

    def update(self, other):  # самый сложный - в other нет совпадающих ключей
        for node in other.nodes_list:
            if self.search(node.key) is None:
                self.add_node(BalancedTreeNode(
                    self.root, node.key, node.value))
            else:
                old_node = self.search(node.key)
                old_node.value = node.value
        return None

    def copy(self):
        new_list_node = []
        for node in self.nodes_list:
            new_node = (node.key, node.value)
            new_list_node.append(new_node)
        new_dict = AVLTreeDict(new_list_node)
        return new_dict

    def __eq__(self, other):  # самый сложный - деревья совпадают
        if len(self.nodes_list) != len(other.nodes_list):
            return False
        for i in range(0, len(self.nodes_list)):
            searched = self.search(other.nodes_list[i].key)
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
        search_result = self.search(key)
        if search_result is None:
            raise KeyError
        self.remove(search_result.key)
        del search_result

    def __iter__(self):
        return self.keys().__iter__()
