import os
import sys
from collections import namedtuple
from Measurer import Measurer
from GraphDataStorage import CurrentData
from GraphicsMaker import GraphicsMaker
from DictsTester import DictsTester
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))
from Dicts.TypesDicts.LinearSearchArrays import ArraysWithLinearSearch
from Dicts.TypesDicts.SortedBinarySearchArrays import BinarySearchArrays
from Dicts.TypesDicts.TreeDict import SimpleTreeDict
from Dicts.TypesDicts.BalancedTreeDict import AVLTreeDict
from Dicts.TypesDicts.HashTableDict import HashTableDict


class Runner:
    def __init__(self, start, step, stop):
        self.start = start
        self.step = step
        self.stop = stop
        self.graphics_maker = GraphicsMaker()
        self.lin_best_data = {'contains': CurrentData('1', 'blue'),
                              'fromkeys': CurrentData('a * x + b', 'blue'),
                              'get': CurrentData('1', 'blue'),
                              'setdefault': CurrentData('1', 'blue'),
                              'pop': CurrentData('a * x + b', 'blue'),
                              'update': CurrentData('a * x + b', 'blue')}
        self.bin_best_data = {'contains': CurrentData('1', 'green'),
                              'fromkeys': CurrentData('a * x + b', 'green'),
                              'get': CurrentData('1', 'green'),
                              'setdefault': CurrentData('a * x + b', 'green'),
                              'pop': CurrentData('1', 'green'),
                              'update': CurrentData('a * lnx + b', 'green')}
        self.tree_best_data = {'contains': CurrentData('1', 'pink'),
                               'fromkeys': CurrentData('a * x + b', 'pink'),
                               'get': CurrentData('1', 'pink'),
                               'setdefault': CurrentData('1', 'pink'),
                               'pop': CurrentData('a * lnx + b', 'pink'),
                               'update': CurrentData('a * x + b', 'pink')}
        self.avl_best_data = {'contains': CurrentData('1', 'yellow'),
                              'fromkeys': CurrentData('a * x + b', 'yellow'),
                              'get': CurrentData('1', 'yellow'),
                              'setdefault': CurrentData('1', 'yellow'),
                              'pop': CurrentData('a * lnx + b', 'yellow'),
                              'update': CurrentData('a * x + b', 'yellow')}
        self.hash_best_data = {'contains': CurrentData('1', 'red'),
                               'fromkeys': CurrentData('a * x + b', 'red'),
                               'get': CurrentData('1', 'red'),
                               'setdefault': CurrentData('1', 'red'),
                               'pop': CurrentData('a * x + b', 'red'),
                               'update': CurrentData('a * x ** b', 'red')}
        self.lin_worst_data = {'contains': CurrentData('a * x + b', 'blue'),
                               'fromkeys': CurrentData('a * x + b', 'blue'),
                               'get': CurrentData('a * x + b', 'blue'),
                               'setdefault': CurrentData('a * x + b', 'blue'),
                               'pop': CurrentData('a * x + b', 'blue'),
                               'update': CurrentData('a * x ** b', 'blue')}
        self.bin_worst_data = {'contains': CurrentData('a * lna + b', 'green'),
                               'fromkeys': CurrentData('a * lna + b', 'green'),
                               'get': CurrentData('a * lna + b', 'green'),
                               'setdefault': CurrentData('a * x + b', 'green'),
                               'pop': CurrentData('a * lna + b', 'green'),
                               'update': CurrentData('a * x ** b', 'green')}
        self.tree_worst_data = {'contains': CurrentData('a * x + b', 'pink'),
                                'fromkeys': CurrentData('a * x + b', 'pink'),
                                'get': CurrentData('a * x + b', 'pink'),
                                'setdefault': CurrentData('a * x + b', 'pink'),
                                'pop': CurrentData('a * x + b', 'pink'),
                                'update': CurrentData('a * x ** b', 'pink')}
        self.avl_worst_data = {'contains': CurrentData(
            'a * lnx + b', 'yellow'),
                               'fromkeys': CurrentData('a * x + b', 'yellow'),
                               'get': CurrentData('a * lnx + b', 'yellow'),
                               'setdefault': CurrentData(
                                    'a * lnx + b', 'yellow'),
                               'pop': CurrentData('a * x + b', 'yellow'),
                               'update': CurrentData('a * lna ** b', 'yellow')}
        self.hash_worst_data = {'contains': CurrentData('a * x + b', 'red'),
                                'fromkeys': CurrentData('a * x + b', 'red'),
                                'get': CurrentData('a * x + b', 'red'),
                                'setdefault': CurrentData('a * x + b', 'red'),
                                'pop': CurrentData('a * x + b', 'red'),
                                'update': CurrentData('a * x ** b', 'red')}
        self.lin_random_data = {'contains': CurrentData('a * x + b', 'blue'),
                                'fromkeys': CurrentData('a * x + b', 'blue'),
                                'get': CurrentData('a * x + b', 'blue'),
                                'setdefault': CurrentData('a * x + b', 'blue'),
                                'pop': CurrentData('a * x + b', 'blue'),
                                'update': CurrentData('a * x ** b', 'blue'),
                                'clear': CurrentData('a * x + b', 'blue'),
                                'copy': CurrentData('a * x + b', 'blue'),
                                'items': CurrentData('a * x + b', 'blue'),
                                'keys': CurrentData('a * x + b', 'blue'),
                                'values': CurrentData('a * x + b', 'blue'),
                                'popitem': CurrentData('a * x ** b', 'blue')}
        self.bin_random_data = {'contains': CurrentData(
            'a * lna + b', 'green'),
                                'fromkeys': CurrentData(
                                    'a * lna + b', 'green'),
                                'get': CurrentData('a * lna + b', 'green'),
                                'setdefault': CurrentData(
                                    'a * x + b', 'green'),
                                'pop': CurrentData('a * lna + b', 'green'),
                                'update': CurrentData('a * x ** b', 'green'),
                                'clear': CurrentData('a * x + b', 'green'),
                                'copy': CurrentData('a * x + b', 'green'),
                                'items': CurrentData('a * x + b', 'green'),
                                'keys': CurrentData('a * x + b', 'green'),
                                'values': CurrentData('a * x + b', 'green'),
                                'popitem': CurrentData('a * x + b', 'green')}
        self.tree_random_data = {'contains': CurrentData('a * x + b', 'pink'),
                                 'fromkeys': CurrentData('a * x + b', 'pink'),
                                 'get': CurrentData('a * x + b', 'pink'),
                                 'setdefault': CurrentData(
                                     'a * x + b', 'pink'),
                                 'pop': CurrentData('a * x + b', 'pink'),
                                 'update': CurrentData('a * x ** b', 'pink'),
                                 'clear': CurrentData('a * x + b', 'pink'),
                                 'copy': CurrentData('a * x + b', 'pink'),
                                 'items': CurrentData('a * x + b', 'pink'),
                                 'keys': CurrentData('a * x + b', 'pink'),
                                 'values': CurrentData('a * x + b', 'pink'),
                                 'popitem': CurrentData('a * x * b', 'pink')}
        self.avl_random_data = {'contains': CurrentData(
            'a * lnx + b', 'yellow'),
                                'fromkeys': CurrentData('a * x + b', 'yellow'),
                                'get': CurrentData('a * lnx + b', 'yellow'),
                                'setdefault': CurrentData(
                                    'a * lnx + b', 'yellow'),
                                'pop': CurrentData('a * x + b', 'yellow'),
                                'update': CurrentData('a * lna + b', 'yellow'),
                                'clear': CurrentData('a * x + b', 'yellow'),
                                'copy': CurrentData('a * x + b', 'yellow'),
                                'items': CurrentData('a * x + b', 'yellow'),
                                'keys': CurrentData('a * x + b', 'yellow'),
                                'values': CurrentData('a * x + b', 'yellow'),
                                'popitem': CurrentData(
                                    'a * lnx + b', 'yellow')}
        self.hash_random_data = {'contains': CurrentData('a * x + b', 'red'),
                                 'fromkeys': CurrentData('a * x + b', 'red'),
                                 'get': CurrentData('a * x + b', 'red'),
                                 'setdefault': CurrentData(
                                     'a * x + b', 'red'),
                                 'pop': CurrentData('a * x + b', 'red'),
                                 'update': CurrentData('a * x ** b', 'red'),
                                 'clear': CurrentData('a * x + b', 'red'),
                                 'copy': CurrentData('a * x + b', 'red'),
                                 'items': CurrentData('a * x + b', 'red'),
                                 'keys': CurrentData('a * x + b', 'red'),
                                 'values': CurrentData('a * x + b', 'red'),
                                 'popitem': CurrentData('a * x + b', 'red')}
        self.best_data = [self.lin_best_data, self.bin_best_data,
                          self.tree_best_data, self.avl_best_data,
                          self.hash_best_data]
        self.random_data = [self.lin_random_data, self.bin_random_data,
                            self.tree_random_data, self.avl_random_data,
                            self.hash_random_data]
        self.worst_data = [self.lin_worst_data, self.bin_worst_data,
                           self.tree_worst_data, self.avl_worst_data,
                           self.hash_worst_data]
        self.types_dict = {ArraysWithLinearSearch: 0,
                           BinarySearchArrays: 1,
                           SimpleTreeDict: 2, AVLTreeDict: 3, HashTableDict: 4}

    def run(self):

        def make_full_data(i, ordered_data, mode):
            modes_dict = {'best': self.best_data,
                          'random': self.random_data,
                          'worst': self.worst_data}
            current_data = modes_dict[mode]
            times = ordered_data[0]
            ints = ordered_data[1]
            for type_dict in self.types_dict:
                for key in times[type_dict]:
                    current_storage = current_data[self.types_dict[type_dict]]
                    if key in current_storage:
                        current_storage[key].append(i, times[
                            type_dict][key][mode], ints[type_dict][key][mode])

        for i in range(self.start, self.stop, self.step):
            measurer = Measurer(i)
            data = measurer.get_information()
            ordered_data = measurer.get_ordered_information(data)

            make_full_data(i, ordered_data, 'best')
            make_full_data(i, ordered_data, 'random')
            make_full_data(i, ordered_data, 'worst')

        self.graphics_maker.make_graphic(self.best_data, 'best')
        self.graphics_maker.make_points_graphic(self.best_data, 'best')
        self.graphics_maker.make_graphic(self.random_data, 'random')
        self.graphics_maker.make_points_graphic(self.random_data, 'random')
        self.graphics_maker.make_graphic(self.worst_data, 'worst')
        self.graphics_maker.make_points_graphic(self.worst_data, 'worst')

        measurer = Measurer(self.stop)
        tester = DictsTester(AVLTreeDict,
                             measurer.make_input_random_data(self.stop),
                             measurer.make_input_increase_data(self.stop))
        memory_data = tester.test_memory()
        self.graphics_maker.make_memory_diagramm(memory_data)


for i in range(2):
    runner = Runner(5, 5, 21)
    runner.run()

runner = Runner(50, 50, 301)
runner.run()
