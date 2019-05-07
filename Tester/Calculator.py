import math
import os
import sys
from copy import deepcopy
from random import randint as rand
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))
from Tester.DataStorage import CurrentData, CurrentTypeStorage, DataStorage
from Dicts.TypesDicts.LinearSearchArrays import ArraysWithLinearSearch
from Dicts.TypesDicts.SortedBinarySearchArrays import BinarySearchArrays
from Dicts.TypesDicts.TreeDict import SimpleTreeDict
from Dicts.TypesDicts.BalancedTreeDict import AVLTreeDict
from Dicts.TypesDicts.HashTableDict import HashTableDict


class Calculator:
    def __init__(self):
        self.types_list = [ArraysWithLinearSearch,
                           BinarySearchArrays, SimpleTreeDict,
                           AVLTreeDict, HashTableDict]
        self.confidence_intervals_dict = {6: 2.5706, 11: 2.2281, 16: 2.1314,
                                          21: 2.0860, 26: 2.0555, 31: 2.0423,
                                          36: 2.0301, 41: 2.0211, 51: 2.0086,
                                          101: 1.9840}
        self.keys = ['clear', 'contains', 'fromkeys', 'copy', 'get', 'items',
                     'keys', 'pop', 'popitem', 'setdefault',
                     'update', 'values']

    def make_current_type_data_storage(self):
        result_tuple = ((CurrentData({}), CurrentData({}), CurrentData({})))
        return CurrentTypeStorage(*result_tuple)

    def make_data_storage(self):
        return DataStorage(*[self.make_current_type_data_storage(),
                             self.make_current_type_data_storage(),
                             self.make_current_type_data_storage(),
                             self.make_current_type_data_storage(),
                             self.make_current_type_data_storage()])

    def calc_average_data(self, data_list):
        current_data = self.make_data_storage()
        result_list = []
        for i in range(len(data_list)):
            current_data += data_list[i]
            result_list.append(deepcopy(current_data) / (i + 1))
        return result_list

    def calc_standart_deviations(self, data, average_data):

        def make_result_list(data, average_data, current_type, result_list):

            def make_first_item(mode):
                if mode == 'random':
                    i = 0
                if mode == 'worst':
                    i = 1
                if mode == 'best':
                    i = 2
                curr_dict = result_list[0][current_type][i]
                first_data = data[1].data_list[types_dict[
                    current_type]].current_data_list[i].data_dict
                second_data = average_data[1].data_list[types_dict[
                    current_type]].current_data_list[i].data_dict
                for key in first_data:
                    curr_dict[key] = math.fabs(
                        first_data[key] - second_data[key])

            types_dict = {ArraysWithLinearSearch: 0,
                          BinarySearchArrays: 1,
                          SimpleTreeDict: 2,
                          AVLTreeDict: 3,
                          HashTableDict: 4}
            make_first_item('random')
            make_first_item('worst')
            make_first_item('best')

            for i in range(1, len(result_list)):
                for j in range(3):
                    for key in self.keys:
                        last_res_quad = result_list[
                            i-1][current_type][j][key] ** 2
                        last_res_quad *= i
                        new_time = data[i+1].data_list[types_dict[
                            current_type]].current_data_list[j].data_dict[key]
                        average_new_time = average_data[i+1].data_list[
                            types_dict[current_type]].current_data_list[
                                    j].data_dict[key]
                        new_member = (new_time - average_new_time) ** 2
                        last_res_quad += new_member
                        last_res_quad /= (i + 1)
                        result_list[i][current_type][j][key] = math.sqrt(
                            last_res_quad)

        data_dict = {ArraysWithLinearSearch: [{}, {}, {}],
                     BinarySearchArrays: [{}, {}, {}],
                     SimpleTreeDict: [{}, {}, {}],
                     AVLTreeDict: [{}, {}, {}],
                     HashTableDict: [{}, {}, {}]}
        result_list = []
        for i in range(1, len(data)):
            result_list.append(data_dict.copy())
        for current_type in self.types_list:
            make_result_list(data, average_data, current_type, result_list)

        return result_list

    def calc_confidence_intervals(self, deviations):
        numbers = [6, 11, 16, 21, 26, 31, 36, 41, 51, 101]
        result_dict = {
            ArraysWithLinearSearch: [{}, {}, {}],
            BinarySearchArrays: [{}, {}, {}],
            SimpleTreeDict: [{}, {}, {}],
            AVLTreeDict: [{}, {}, {}],
            HashTableDict: [{}, {}, {}]}
        for dict_type in self.types_list:
            for i in range(len(numbers)):
                for j in range(3):
                    for key in self.keys:
                        try:
                            number = numbers[i]
                            conf_interval = self.confidence_intervals_dict[
                                number] * deviations[
                                number - 3][dict_type][j][
                                    key] / math.sqrt(number)
                            result_dict[dict_type][j][key] = conf_interval
                        except IndexError:
                            print('i = ' + str(i))
                            print('number = ' + str(number))
                            print('j = ' + str(j))
                            print('key = ' + str(key))
                            sys.exit()
        return result_dict
