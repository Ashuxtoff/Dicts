import os
import sys
import unittest
from random import randint
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))
from Dicts.TypesDicts.TreeDict import SimpleTreeDict
from Dicts.TypesDicts.BalancedTreeDict import AVLTreeDict
from Tester.Calculator import Calculator
from Tester.DataStorage import DataStorage, CurrentData, CurrentTypeStorage


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

        def create_current_type_storage(value):
            base_dict = {"clear": value, "contains": value,
                         "fromkeys": value, "copy": value, "get": value,
                         "items": value, "keys": value,
                         "pop": value, "popitem": value,
                         "setdefault": value,
                         "update": value, "values": value}
            init_tuple = (CurrentData(base_dict.copy()),
                          CurrentData(base_dict.copy()),
                          CurrentData(base_dict.copy()))
            return CurrentTypeStorage(*init_tuple)

        self.data_list = [DataStorage(create_current_type_storage(
            randint(0, 4)),
                                      create_current_type_storage(
                                          randint(0, 4)),
                                      create_current_type_storage(
                                          randint(0, 4)),
                                      create_current_type_storage(
                                          randint(0, 4)),
                                      create_current_type_storage(
                                          randint(0, 4))) for i in range(5)]

    def test_calc_average_data(self):
        average_data = self.calculator.calc_average_data(self.data_list)
        self.assertEqual(len(self.data_list), len(average_data))
        self.assertEqual(average_data[2].lin_data.best.data_dict["clear"],
                         (self.data_list[0].lin_data.best.data_dict["clear"]
                          + self.data_list[1].lin_data.best.data_dict["clear"]
                          + self.data_list[2].lin_data.best.data_dict[
                              "clear"]) / 3)

    def test_calc_standart_deviations(self):
        average_data = self.calculator.calc_average_data(self.data_list)
        res = self.calculator.calc_standart_deviations(
            self.data_list, average_data)
        self.assertNotEqual(res[0][AVLTreeDict][0]['clear'], None)
        self.assertNotEqual(res[0][SimpleTreeDict][0]['clear'], None)


if __name__ == '__main__':
    unittest.main()
