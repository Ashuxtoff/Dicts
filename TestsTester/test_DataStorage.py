import unittest
import os
import sys
from copy import deepcopy
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))
from Tester.DataStorage import DataStorage, CurrentTypeStorage, CurrentData


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
