import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))
from Tester.Measurer import Measurer
from Tester.DataStorage import DataStorage, CurrentData, CurrentTypeStorage


class TestMeasurer(unittest.TestCase):
    def setUp(self):
        self.measurer = Measurer(20)

    def test_initialize(self):
        self.assertEqual(
            len(self.measurer.random_data), self.measurer.data_length)
        self.assertEqual(
            len(self.measurer.increase_data), self.measurer.data_length)

    def test_measure_data(self):
        result = self.measurer.measure_data()
        self.assertFalse(os.stat('random20.txt') == 0)

    def test_afile_write(self):
        data_tuple_1 = tuple([CurrentData({}) for i in range(3)])
        data_tuple_2 = tuple([
            CurrentTypeStorage(*data_tuple_1) for i in range(5)])
        data = [DataStorage(*data_tuple_2) for i in range(3)]
        self.measurer.file_write(data)
        self.assertEqual(sum(1 for line in open('best20.txt', 'r')), 180)

    def test_file_parse(self):
        result = self.measurer.file_parse('best20.txt', 'random20.txt',
                                          'worst20.txt')
        self.assertEqual(len(result), 3)

    # def test_get_ordered_information(self):
    #     ordered_information = self.measurer.get_ordered_information(
    #         self.measurer.get_information())
    #     times = ordered_information[0]
    #     ints = ordered_information[1]
    #     self.assertEqual(type(times[AVLTreeDict]['clear']['best']), float)
    #     self.assertEqual(type(ints[AVLTreeDict]['clear']['random']), float)


if __name__ == '__main__':
    unittest.main()
