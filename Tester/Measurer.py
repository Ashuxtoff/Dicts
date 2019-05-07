import os
import sys
import random
import string
import inspect
from linecache import getline
from collections import namedtuple
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))
from Tester.DictsTester import DictsTester
from Tester.Calculator import Calculator
from Tester.DataStorage import CurrentData, CurrentTypeStorage, DataStorage
from Dicts.TypesDicts.LinearSearchArrays import ArraysWithLinearSearch
from Dicts.TypesDicts.SortedBinarySearchArrays import BinarySearchArrays
from Dicts.TypesDicts.TreeDict import SimpleTreeDict
from Dicts.TypesDicts.BalancedTreeDict import AVLTreeDict
from Dicts.TypesDicts.HashTableDict import HashTableDict


class Measurer:
    def make_input_random_data(self, length):
        result = []
        for i in range(length):
            key = ''.join(random.choice(
                string.ascii_letters + string.digits) for i in range(3))
            value = random.randint(1, 1000)
            result.append((key, value))
        return result

    def make_input_increase_data(self, length):
        result = self.make_input_random_data(length)
        return sorted(result)

    def __init__(self, data_length):
        self.calculator = Calculator()
        self.data_length = data_length
        self.random_data = self.make_input_random_data(data_length)
        self.increase_data = self.make_input_increase_data(data_length)
        self.types_dict = [ArraysWithLinearSearch,
                           BinarySearchArrays,
                           SimpleTreeDict, AVLTreeDict, HashTableDict]

    def file_write(self, input_data):
        with open('random' + str(self.data_length) + '.txt', 'w') as r, open(
            'worst' + str(self.data_length) + '.txt', 'w') as w, open(
                'best' + str(self.data_length) + '.txt', 'w') as b:
            files = [r, w, b]
            dict_names = ['lin', 'bin', 'tree', 'avl', 'hash']
            type_names = ['random', 'worst', 'best']
            for data in input_data:
                for i in range(len(data.data_list)):
                    name_dict = dict_names[i]
                    types = data.data_list[i].current_data_list
                    for j in range(len(types)):
                        name_type = type_names[j]
                        time_dict = types[j].data_dict
                        for key in time_dict:
                            line = name_dict + ' ' + name_type + ' ' + key \
                                + ' ' + str(time_dict[key]) + '\n'
                            files[j].write(line)

    def file_parse(self, best, random, worst):
        with open(best, 'r') as b, open(
            random, 'r') as r, open(
                worst, 'r') as w:
            result_list = []
            type_data_list = []
            files_length = sum(1 for line in b)
            best_data = CurrentData({})
            random_data = CurrentData({})
            worst_data = CurrentData({})
            for i in range(files_length):
                if i > 0 and getline(best, i+1)[0] != getline(
                        best, i)[0] or i == files_length-1:
                        type_data_list.append(CurrentTypeStorage(
                            random_data, worst_data, best_data))
                        best_data = CurrentData({})
                        random_data = CurrentData({})
                        worst_data = CurrentData({})
                best_splitted_line = getline(best, i+1).split(' ')
                random_splitted_line = getline(random, i+1).split(' ')
                worst_splitted_line = getline(worst, i+1).split(' ')
                best_data.data_dict[best_splitted_line[2]] = float(
                    best_splitted_line[3][:-1])
                random_data.data_dict[random_splitted_line[2]] = float(
                    random_splitted_line[3][:-1])
                worst_data.data_dict[worst_splitted_line[2]] = float(
                    worst_splitted_line[3][:-1])
                if len(type_data_list) == 5:
                    result_list.append(DataStorage(type_data_list[0],
                                                   type_data_list[1],
                                                   type_data_list[2],
                                                   type_data_list[3],
                                                   type_data_list[4]))
                    type_data_list.clear()
        return result_list

    def measure_data(self):
        file_name = 'random' + str(self.data_length) + '.txt'
        a = os.path.exists(file_name)
        if not os.path.exists(file_name) or os.stat(file_name) == 0:
            final_data = []
            random_input = self.make_input_random_data(self.data_length)
            increase_input = self.make_input_increase_data(self.data_length)
            for i in range(101):
                results = []
                for type_dict in self.types_dict:
                    tester = DictsTester(
                        type_dict, random_input, increase_input)
                    random_data = CurrentData(
                        tester.test_common_funcs())
                    best_data = CurrentData(
                        tester.test_extreme_funcs("best"))
                    worst_data = CurrentData(
                        tester.test_extreme_funcs("worst"))
                    results.append(CurrentTypeStorage(
                        random_data, worst_data, best_data))
                final_data.append(DataStorage(results[0], results[1],
                                              results[2],
                                              results[3], results[4]))
            self.file_write(final_data)

    def get_information(self):
        self.measure_data()
        measuring_result = self.file_parse(
            'best' + str(self.data_length) + '.txt',
            'random' + str(self.data_length) + '.txt',
            'worst' + str(self.data_length) + '.txt')
        average_data = self.calculator.calc_average_data(measuring_result)
        standart_deviations = self.calculator.calc_standart_deviations(
            measuring_result, average_data)
        confidence_interval = self.calculator.calc_confidence_intervals(
            standart_deviations)
        result_form = namedtuple('result',
                                 'average_time conf_interval stand_dev')
        result = result_form(average_data, confidence_interval,
                             standart_deviations)
        return result

    def get_ordered_information(self, information):

        data = information.average_time[-1]
        ints = information.conf_interval
        lin_data = data.lin_data
        bin_data = data.bin_data
        tree_data = data.tree_data
        avl_data = data.avl_data
        hash_data = data.hash_data
        data_dict = {ArraysWithLinearSearch: lin_data,
                     BinarySearchArrays: bin_data,
                     SimpleTreeDict: tree_data,
                     AVLTreeDict: avl_data,
                     HashTableDict: hash_data}
        result_dict = {}
        result_ints_dict = {}
        for type_dict in self.types_dict:
            result_dict[type_dict] = {}
            clear = {'best': data_dict[type_dict].best.data_dict["clear"],
                     'random': data_dict[type_dict].random.data_dict["clear"],
                     'worst': data_dict[type_dict].worst.data_dict["clear"]}
            contains = {'best': data_dict[type_dict].best.data_dict[
                "contains"],
                        'random': data_dict[type_dict].random.data_dict[
                            "contains"],
                        'worst': data_dict[type_dict].worst.data_dict[
                            "contains"]}
            fromkeys = {'best': data_dict[type_dict].best.data_dict[
                "fromkeys"],
                        'random': data_dict[type_dict].random.data_dict[
                            "fromkeys"],
                        'worst': data_dict[type_dict].worst.data_dict[
                            "fromkeys"]}
            copy = {'best': data_dict[type_dict].best.data_dict["copy"],
                    'random': data_dict[type_dict].random.data_dict["copy"],
                    'worst': data_dict[type_dict].worst.data_dict["copy"]}
            get = {'best': data_dict[type_dict].best.data_dict["get"],
                   'random': data_dict[type_dict].random.data_dict["get"],
                   'worst': data_dict[type_dict].worst.data_dict["get"]}
            items = {'best': data_dict[type_dict].best.data_dict["items"],
                     'random': data_dict[type_dict].random.data_dict["items"],
                     'worst': data_dict[type_dict].worst.data_dict["items"]}
            keys = {'best': data_dict[type_dict].best.data_dict["keys"],
                    'random': data_dict[type_dict].random.data_dict["keys"],
                    'worst': data_dict[type_dict].worst.data_dict["keys"]}
            pop = {'best': data_dict[type_dict].best.data_dict["pop"],
                   'random': data_dict[type_dict].random.data_dict["pop"],
                   'worst': data_dict[type_dict].worst.data_dict["pop"]}
            popitem = {'best': data_dict[type_dict].best.data_dict["popitem"],
                       'random': data_dict[type_dict].random.data_dict[
                           "popitem"],
                       'worst': data_dict[type_dict].worst.data_dict[
                           "popitem"]}
            setdefault = {'best': data_dict[type_dict].best.data_dict[
                "setdefault"],
                          'random': data_dict[type_dict].random.data_dict[
                              "setdefault"],
                          'worst': data_dict[type_dict].worst.data_dict[
                              "setdefault"]}
            update = {'best': data_dict[type_dict].best.data_dict["update"],
                      'random': data_dict[type_dict].random.data_dict[
                          "update"],
                      'worst': data_dict[type_dict].worst.data_dict["update"]}
            values = {'best': data_dict[type_dict].best.data_dict["values"],
                      'random': data_dict[type_dict].random.data_dict[
                          "values"],
                      'worst': data_dict[type_dict].worst.data_dict["values"]}

            time_dict = result_dict[type_dict]
            time_dict.update([('clear', clear), ('copy', copy),
                              ('contains', contains), ('fromkeys', fromkeys),
                              ('get', get), ('items', items),
                              ('keys', keys), ('pop', pop),
                              ('popitem', popitem),
                              ('setdefault', setdefault), ('update', update),
                              ('values', values)])

            clear_int = {'best': ints[type_dict][0]['clear'],
                         'random': ints[type_dict][1]['clear'],
                         'worst': ints[type_dict][2]['clear']}
            contains_int = {'best': ints[type_dict][0]['contains'],
                            'random': ints[type_dict][1]['contains'],
                            'worst': ints[type_dict][2]['contains']}
            fromkeys_int = {'best': ints[type_dict][0]['fromkeys'],
                            'random': ints[type_dict][1]['fromkeys'],
                            'worst': ints[type_dict][2]['fromkeys']}
            copy_int = {'best': ints[type_dict][0]['copy'],
                        'random': ints[type_dict][1]['copy'],
                        'worst': ints[type_dict][2]['copy']}
            get_int = {'best': ints[type_dict][0]['get'],
                       'random': ints[type_dict][1]['get'],
                       'worst': ints[type_dict][2]['get']}
            items_int = {'best': ints[type_dict][0]['items'],
                         'random': ints[type_dict][1]['items'],
                         'worst': ints[type_dict][2]['items']}
            keys_int = {'best': ints[type_dict][0]['keys'],
                        'random': ints[type_dict][1]['keys'],
                        'worst': ints[type_dict][2]['keys']}
            pop_int = {'best': ints[type_dict][0]['pop'],
                       'random': ints[type_dict][1]['pop'],
                       'worst': ints[type_dict][2]['pop']}
            popitem_int = {'best': ints[type_dict][0]['popitem'],
                           'random': ints[type_dict][1]['popitem'],
                           'worst': ints[type_dict][2]['popitem']}
            setdefault_int = {'best': ints[type_dict][0]['setdefault'],
                              'random': ints[type_dict][1]['setdefault'],
                              'worst': ints[type_dict][2]['setdefault']}
            update_int = {'best': ints[type_dict][0]['update'],
                          'random': ints[type_dict][1]['update'],
                          'worst': ints[type_dict][2]['update']}
            values_int = {'best': ints[type_dict][0]['values'],
                          'random': ints[type_dict][1]['values'],
                          'worst': ints[type_dict][2]['values']}

            result_ints_dict[type_dict] = {}
            ints_dict = result_ints_dict[type_dict]
            ints_dict.update([('clear', clear_int), ('copy', copy_int),
                             ('contains', contains_int),
                             ('fromkeys', fromkeys_int),
                             ('get', get_int), ('items', items_int),
                             ('keys', keys_int), ('pop', pop_int),
                             ('popitem', popitem_int),
                             ('setdefault', setdefault_int),
                             ('update', update_int), ('values', values_int)])

        return_form = namedtuple('return_form', 'time, ints')
        return return_form(result_dict, result_ints_dict)
