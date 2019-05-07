import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))
import random
from DictsOrganizations.DictBase import DictBase


class ArraysWithLinearSearch(DictBase):
    def __init__(self, tuples_list=[]):
        self.keys_list = []
        self.values_list = []
        for item in tuples_list:
            self.keys_list.append(item[0])
            self.values_list.append(item[1])

    def __getitem__(self, key):
        for i in range(len(self.keys_list)):
            if self.keys_list == key:
                return self.values_list[i]
        return None

    def __contains__(self, needed_key):  # самое сложное - поиск последнего
        for key in self.keys_list:
            if key == needed_key:
                return True
        return False

    def clear(self):
        while len(self.keys_list) > 0:  # один результат
            del self.keys_list[0]
            del self.values_list[0]

    def fromkeys(self, sequence, value=None):  # один результат
        self.clear()
        for element in sequence:
            self.keys_list.append(element)
            self.values_list.append(value)

    def get(self, needed_key, default=None):
        i = 0
        while i < len(self.keys_list) and self.keys_list[i] != needed_key:
            i += 1   # cамое сложное - гет последнего
        if i < len(self.keys_list):
            return self.values_list[i]
        return default

    def items(self):  # один резуьтат
        pairs = []
        for i in range(len(self.keys_list)):
            pairs.append((self.keys_list[i], self.values_list[i]))
        return pairs

    def keys(self):  # один результат
        return self.keys_list

    def popitem(self):  # сущность функции рандомизирует результат
        if len(self.keys_list) == 0:
            raise KeyError
        number = self.keys_list[random.randint(0, len(self.keys_list)-1)]
        i = 0
        while i < len(self.values_list):
            if self.keys_list[i] == number:
                needed_key = self.keys_list[i]
                needed_value = self.values_list[i]
                self.keys_list.remove(needed_key)
                self.values_list.remove(needed_value)
                return (needed_key, needed_value)
            i += 1

    def setdefault(self, needed_key, value=None):  # нет плюча
        for i in range(len(self.keys_list)):
            if self.keys_list[i] == needed_key:
                return self.values_list[i]
        self.keys_list.append(needed_key)
        self.values_list.append(value)
        return value

    def pop(self, needed_key, default=None):  # самое сложное - последний ключ?
        if needed_key is None:  # или самое сложное - первый ключ?
            # raise KeyError
            return None
        for i in range(len(self.keys_list)):
            if self.keys_list[i] == needed_key:
                self.keys_list.remove(needed_key)
                key_value = self.values_list[i]
                self.values_list.remove(key_value)
                return key_value
        return default

    def values(self):  # один результат
        values = []
        for value in self.values_list:
            values.append(value)
        return values

    def update(self, other):  # ключи other и self совпадают - самое сложное
        for i in range(len(other.keys_list)):
            if self.keys_list.__contains__(other.keys_list[i]):
                for i in range(len(self.keys_list)):
                    if len(other.keys_list) > i:
                        if self.keys_list[i] == other.keys_list[i]:
                            self.values_list[i] = other.values_list[i]
            else:
                self.keys_list.append(other.keys_list[i])
                self.values_list.append(other.values_list[i])
        return None

    def copy(self):  # один результат
        tuples_list = []
        for i in range(len(self.keys_list)):
            tuples_list.append((self.keys_list[i], self.values_list[i]))
        new_dict = ArraysWithLinearSearch(tuples_list)
        return new_dict

    def __eq__(self, other):  # самое простое - разные длины
        if len(self.keys_list) != len(other.keys_list):  # сложное - равны
            return False
        for i in range(len(self.keys_list)):
            if self.keys_list[i] != other.keys_list[i] \
                    or self.values_list[i] != other.values_list[i]:
                return False
        return True

    def __len__(self):  # один результат
        return len(self.keys_list)

    def __iter__(self):  # один результат
        return self.keys_list.__iter__()

    def __delitem__(self, key):  # удаление последнего - самое сложное
        for i in range(len(self.keys_list)):
            if self.keys_list[i] == key:
                del self.keys_list[i]
                del self.values_list[i]
                break
