import random
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))
from DictsOrganizations.DictBase import DictBase
from DictsOrganizations.BinarySearch import BinarySearch


class BinarySearchArrays(DictBase):
    def __init__(self, tuples_list=[]):
        self.keys_list = []
        self.values_list = []
        for item in tuples_list:
            self.keys_list.append(item[0])
            self.values_list.append(item[1])

    def __getitem__(self, key):
        if BinarySearch(key, self.keys_list) is None:
            return None
        return self.values_list[BinarySearch(key, self.keys_list)]

    def __contains__(self, needed_key):  # самый сложный случай - нет искомого
        return BinarySearch(needed_key, self.keys_list) is not None

    def clear(self):  # один результат
        while len(self.keys_list) > 0:
            del self.keys_list[0]
            del self.values_list[0]

    def fromkeys(self, sequence, value=None):  # обратный порядок sequencе
        self.clear()  # самый простой - отсротированная sequence
        sequence.sort()
        for element in sequence:
            self.keys_list.append(element)
            self.values_list.append(value)

    def get(self, needed_key, default=None):  # самый сложный - нет искомого
        if BinarySearch(needed_key, self.keys_list) is not None:
            return self.values_list[BinarySearch(
                needed_key, self.keys_list, True)]
        else:
            return default

    def items(self):  # один результат
        pairs = []
        for i in range(len(self.keys_list)):
            pairs.append((self.keys_list[i], self.values_list[i]))
        return pairs

    def keys(self):  # один результат
        return self.keys_list

    def popitem(self):  # сущность функции рандомизирует результат
        if len(self.keys_list) == 0:
            raise KeyError
        number = random.randint(0, len(self.keys_list)-1)
        needed_key = self.keys_list[number]
        index = BinarySearch(needed_key, self.keys_list, True)
        key = self.keys_list[index]
        value = self.values_list[index]
        self.keys_list.remove(key)
        self.values_list.remove(value)
        return (key, value)

    def setdefault(self, needed_key, value=None):  # сложный - нет искомого
        if BinarySearch(needed_key, self.keys_list) is not None:
            index = BinarySearch(needed_key, self.keys_list, True)
            return self.values_list[index]
        else:
            self.keys_list.append(needed_key)
            self.keys_list.sort()
            index = self.keys_list.index(needed_key)
            self.values_list.insert(index, value)
            return value

    def pop(self, needed_key, default=None):  # сложный случай - ключ есть
        if needed_key is None:
            # raise KeyError
            return None
        if BinarySearch(needed_key, self.keys_list) is None:
            return default
        value = self.values_list[BinarySearch(
            needed_key, self.keys_list, True)]
        self.keys_list.remove(
            self.keys_list[BinarySearch(needed_key, self.keys_list, True)])
        self.values_list.remove(value)
        return value

    def values(self):  # один результат
        values = []
        for value in self.values_list:
            values.append(value)
        return values

    def update(self, other):  # other отличен от self полностью
        for i in range(len(other.keys_list)):
            index = BinarySearch(other.keys_list[i], self.keys_list, True)
            if self.keys_list[index] != other.keys_list[i]:
                self.keys_list.insert(index, other.keys_list[i])
                self.values_list.insert(index, other.values_list[i])
            else:
                self.values_list[index] = other.values_list[i]
        return None

    def copy(self):  # один результат
        tuples_list = []
        for i in range(len(self.keys_list)):
            tuples_list.append((self.keys_list[i], self.values_list[i]))
        new_dict = BinarySearchArrays(tuples_list)
        return new_dict

    def __eq__(self, other):  # один результат
        if len(self.keys_list) != len(other.keys_list):
            return False
        for i in range(len(self.keys_list)):
            if self.keys_list[i] != other.keys_list[i] \
               or self.values_list[i] != other.values_list[i]:
                    return False
        return True

    def __len__(self):
        return len(self.keys_list)

    def __iter__(self):
        return self.keys_list.__iter__()

    def __delitem__(self, key):
        for i in range(len(self.keys_list)):
            if self.keys_list[i] == key:
                del self.keys_list[i]
                del self.values_list[i]
                break
