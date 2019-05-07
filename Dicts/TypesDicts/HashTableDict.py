import copy
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))
import random
from DictsOrganizations.DictBase import DictBase
from DictsOrganizations.HashTable import HashTable
from DictsOrganizations.HashTable import HashTableItem


class HashTableDict(HashTable, DictBase):
    def __init__(self, tuple_list=None):
        super().__init__()
        self.tuples_list = tuple_list
        if tuple_list is not None:
            for item in tuple_list:
                self.add(HashTableItem(item[0], item[1]))

    def __getitem__(self, key):
        return self.search(key)

    def __contains__(self, needed_key):  # самый сложный - ключ последний в
        if self.search(needed_key) is None:  # самом длинного ряда коллизий
            return False
        return True

    def clear(self):  # на одном размере будет все одинаково
        flag = False
        founded = 0
        for j in range(1, self.size_width):
            for i in range(self.size_height):
                if self.hash_table[i][j] is not None:
                    founded += 1
                    self.remove(self.hash_table[i][j].key)
                    if founded == self.engaged:
                        flag = True
                        break
            if flag:
                break

    def fromkeys(self, sequence, value=None):  # самое сложное - у всех эл-в
        self.clear()  # из sequence одинаковый хеш
        for i in range(len(sequence)):
            new_item = HashTableItem(sequence[i], value)
            self.add(new_item)

    def get(self, needed_key, default=None):  # сложно -  нет искомого ключа
        if self.search(needed_key) is None:
            return default
        else:
            return self.search(needed_key).value

    def items(self):
        flag = False
        founded = 0
        pairs = []
        for j in range(1, self.size_width):
            for i in range(self.size_height):
                if self.hash_table[i][j] is not None:
                    item = self.hash_table[i][j]
                    pairs.append((item.key, item.value))
                    founded += 1
                    if founded == self.engaged:
                        flag = True
                        break
            if flag:
                break
        return pairs

    def keys(self):
        flag = False
        founded = 0
        keys = []
        for i in range(self.size_height):
            for j in range(1, self.size_width):
                if self.hash_table[i][j] is not None:
                    item = self.hash_table[i][j]
                    keys.append(item.key)
                    founded += 1
                    if founded == self.engaged:
                        flag = True
                        break
            if flag:
                break
        return keys

    def popitem(self):  # рандомизирован
        if self.engaged == self.size_height:
            raise KeyError
        index = random.randint(0, self.engaged - self.size_height - 1)
        keys = self.keys()
        key = keys[index]
        value = self.search(key)
        self.remove(key)
        return (key, value)

    def setdefault(self, needed_key, value=None):  # нет искомого ключа и его
        if self.search(needed_key) is None:  # хеш равен значению самой длинной
            self.add(HashTableItem(needed_key, value))  # коллизионной строчки
        return self.search(needed_key).value

    def pop(self, needed_key, default=None):  # последний в самой длинной
        if needed_key is None:  # коллизионной строчке
            # raise KeyError
            return None
        needed_node = self.search(needed_key)
        if needed_node is None:
            return default
        needed_value = needed_node.value
        self.remove(needed_node.key)
        return needed_value

    def values(self):
        flag = False
        founded = 0
        values = []
        for j in range(1, self.size_width):
            for i in range(self.size_height):
                if self.hash_table[i][j] is not None:
                    item = self.hash_table[i][j]
                    values.append(item.value)
                    founded += 1
                    if founded == self.engaged:
                        flag = True
                        break
            if flag:
                break
        return values

    def update(self, other):  # хэштаблицы одних размеров
        founded = 0  # other полностью отличен по ключам от self
        flag = False
        for i in range(0, other.size_width):
            for j in range(0, other.size_height):
                if other.hash_table[j][i] is not None:
                    if self.search(other.hash_table[j][i].key) is not None:
                        founded += 1
                    else:
                        new_item = HashTableItem(
                            other.hash_table[j][i].key,
                            other.hash_table[j][i].value)
                        self.add(new_item)
                    if founded == other.engaged:
                        flag = True
                        break
            if flag:
                break

    def copy(self):
        return HashTableDict(self.tuples_list)

    def __eq__(self, other):
        if self.size_height != other.size_height \
           or self.size_width != other.size_width \
           or self.engaged != other.engaged:
                return False
        flag = False
        founded = 0
        for i in range(self.size_width):
            for j in range(self.size_height):
                item1 = self.hash_table[j][i]
                item2 = other.hash_table[j][i]
                if item1 is None:
                    if item2 is not None:
                        return False
                if item2 is None:
                    if item1 is not None:
                        return False
                if item1 is not None and item2 is not None:
                    if item1.next is not None and item2.next is not None:
                        if item1.key == item2.key and \
                           item1.value == item2.value and \
                           item1.next.key == item2.next.key:
                                founded += 1
                                if founded == self.engaged:
                                    flag = True
                                    break
                        else:
                            return False
            if flag:
                break
        return True

    def __len__(self):
        return self.engaged - self.size_height

    def __delitem__(self, key):
        item = self.search(key)
        if item is None:
            raise KeyError
        self.remove(key)

    def __iter__(self):
        keys = self.keys()
        return keys.__iter__()
