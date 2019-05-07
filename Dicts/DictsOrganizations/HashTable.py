import unittest
from copy import deepcopy


class HashTableItem():
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class HashTable():
    def __init__(self, size_height=10, size_width=5):  # для облегчения теста
        self.max_load_factor = 0.66
        self.size_height = size_height
        self.size_width = size_width
        self.size = size_height*size_width
        self.engaged = size_height
        self.lengths = []
        self.hash_table = []
        for i in range(size_height):
            new_table = [HashTableItem()]
            self.lengths.append(0)
            for j in range(size_width-1):
                new_table.append(None)
            self.hash_table.append(new_table)

    def balance(self):
            for i in range(self.size_height):
                new_list = []
                for j in range(self.size_width):
                    if self.hash_table[i][j] is not None:
                        new_list.append(self.hash_table[i][j])
                    else:
                        new_list.append(None)
                for k in range(self.size_width):
                    new_list.append(None)
                del self.hash_table[i]
                self.hash_table.insert(i, new_list)
            self.size *= 2
            self.size_width *= 2

    def get_hash(self, key):
        return hash(key) % self.size_height

    def add(self, item):
        key_hash = self.get_hash(item.key)
        self.lengths[key_hash] += 1
        if self.hash_table[key_hash][self.size_width-1] is not None:
            self.balance()
        if self.hash_table[key_hash][0] is None:
            self.hash_table[key_hash][0] = (item)
        else:
            current = self.hash_table[key_hash][0]
            while current.next is not None:  # ищем, куда бы прилепить как
                current = current.next  # как дочерний
            i = self.hash_table[key_hash].index(None)
            # while self.hash_table[key_hash][i] is not None:  # Ищем первое
            #     i += 1  # свободное место в листе
            self.hash_table[key_hash][i] = item
            current.next = item
        self.engaged += 1
        load_factor = self.engaged / self.size
        if load_factor >= self.max_load_factor:
            self.balance()

    def search(self, needed_key):
        key_hash = self.get_hash(needed_key)
        collisions = self.hash_table[key_hash]
        for item in collisions:
            if item is not None:
                if item.key == needed_key:
                    return item
        return None

    def remove(self, needed_key):
        self.engaged -= 1
        key_hash = self.get_hash(needed_key)
        collisions = self.hash_table[key_hash]
        for item in collisions:
            if item is not None:
                if item.next is not None:
                    if item.next.key == needed_key:
                        index = collisions.index(item.next)
                        if item.next.next is not None:
                            item.next = item.next.next
                        else:
                            item.next = None
                        collisions[index] = None
                        return None
        return None

    def get_longest_collision(self):
        max_collisions_length = max(self.lengths)
        return self.lengths.index(max_collisions_length)


class TestDataStorage(unittest.TestCase):
    def setUp(self):
        self.c_d_1 = CurrentData({})
        self.c_d_2 = CurrentData({})
        for key in self.c_d_1.data_dict:
            self.c_d_1.data_dict[key] = 1
            self.c_d_2.data_dict[key] = 2
        self.c_t_s_1 = CurrentTypeStorage(deepcopy(self.c_d_1),
                                          deepcopy(self.c_d_1),
                                          deepcopy(self.c_d_1))
        self.c_t_s_2 = CurrentTypeStorage(deepcopy(self.c_d_2),
                                          deepcopy(self.c_d_2),
                                          deepcopy(self.c_d_2))
        self.d_s_1 = DataStorage(deepcopy(self.c_t_s_1),
                                 deepcopy(self.c_t_s_1),
                                 deepcopy(self.c_t_s_1),
                                 deepcopy(self.c_t_s_1),
                                 deepcopy(self.c_t_s_1))
        self.d_s_2 = DataStorage(deepcopy(self.c_t_s_2),
                                 deepcopy(self.c_t_s_2),
                                 deepcopy(self.c_t_s_2),
                                 deepcopy(self.c_t_s_2),
                                 deepcopy(self.c_t_s_2))

    def test_current_data(self):
        self.c_d_1 += self.c_d_2
        for key in self.c_d_1.data_dict:
            self.assertEqual(self.c_d_1.data_dict[key], 3)
        self.c_d_1 /= 3
        for key in self.c_d_1.data_dict:
            self.assertEqual(self.c_d_1.data_dict[key], 1)

    def test_curent_type_storage(self):
        self.c_t_s_1 += self.c_t_s_2
        for data in self.c_t_s_1.current_data_list:
            for key in data.data_dict:
                self.assertEqual(data.data_dict[key], 3)
        self.c_t_s_1 /= 3
        for data in self.c_t_s_1.current_data_list:
            for key in data.data_dict:
                self.assertEqual(data.data_dict[key], 1)

    def test_data_strorage(self):
        self.d_s_1 += self.d_s_2
        for curr_data in self.d_s_1.data_list:
            for data in curr_data.current_data_list:
                for key in data.data_dict:
                    self.assertEqual(data.data_dict[key], 3)
        self.d_s_1 /= 3
        for curr_data in self.d_s_1.data_list:
            for data in curr_data.current_data_list:
                for key in data.data_dict:
                    self.assertEqual(data.data_dict[key], 1)


if __name__ == '__main__':
    unittest.main()
