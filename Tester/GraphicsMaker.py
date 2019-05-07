import os
import sys
import math
import matplotlib.pyplot as plt
from FuncsApproximator import FuncsApproximator
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))
from Dicts.TypesDicts.BalancedTreeDict import AVLTreeDict
from Dicts.TypesDicts.HashTableDict import HashTableDict
from Dicts.TypesDicts.LinearSearchArrays import ArraysWithLinearSearch
from Dicts.TypesDicts.SortedBinarySearchArrays import BinarySearchArrays
from Dicts.TypesDicts.TreeDict import SimpleTreeDict


class GraphicsMaker:
    def __init__(self):
        self.approximator = FuncsApproximator()
        self.all_keys = ['clear', 'copy', 'contains', 'fromkeys', 'items',
                         'keys', 'pop', 'popitem', 'setdefault', 'values',
                         'update', 'get']
        self.extreme_keys = ['get', 'contains', 'setdefault',
                             'fromkeys', 'pop', 'update']

    def make_graphic(self, data_list, pattern):
        plt.clf()
        if pattern == 'best' or pattern == 'worst':
            keys_list = self.extreme_keys
        else:
            keys_list = self.all_keys
        for key in keys_list:
            plt.clf()
            for data in data_list:
                if data[key].appr_type == 'a * lnx + b':
                    a, b = self.approximator.log_approximate(data[key])
                    plt.plot([i for i in range(
                             2, max(list(data[key].points.keys())) + 2)],
                             [a * math.log1p(i - 1) + max([
                                 0, b]) for i in range(2, max(list(
                                     data[key].points.keys())) + 2)],
                             data[key].color)
                if data[key].appr_type == 'a * x ** b':
                    a, b = self.approximator.pow_approximate(data[key])
                    plt.plot([i for i in range(
                             max(list(data[key].points.keys())) + 2)],
                             [a * (i ** b) for i in range(
                                 max(list(data[key].points.keys())) + 2)],
                             data[key].color)
                if data[key].appr_type == 'a * x + b':
                    appr_dict = {number: data[key].points[
                        number].y for number in data[key].points}
                    a, b = self.approximator.lin_approximate(appr_dict)
                    plt.plot([i for i in range(
                        max(list(data[key].points.keys())))],
                             [a * i + max([0, b]) for i in range(
                                 max(list(data[key].points.keys())))],
                             data[key].color)
                if data[key].appr_type == 'a * lna + b':
                    appr_dict = {number: data[key].points[
                        number].y for number in data[key].points}
                    a, b = self.approximator.lin_approximate(appr_dict)
                    plt.plot([i for i in range(
                        2, max(list(data[key].points.keys())) + 2)],
                             [a * i * math.log1p(i - 1) + max(
                                 [0, b]) for i in range(
                                 2, max(list(data[key].points.keys())) + 2)],
                             data[key].color)
                if data[key].appr_type == '1':
                    average_time = 0
                    for number in data[key].points:
                        average_time += data[key].points[number].y
                    average_time /= len(data[key].points)
                    plt.plot([i for i in range(max(list(
                        data[key].points.keys())))],
                              [average_time for i in range(max(
                                  list(data[key].points.keys())))], data[
                                      key].color)
            # plt.xlabel('Размер данных')
            # plt.ylabel('Время работы')
            # plt.show()
            plt.savefig(pattern + '_' + key + '_appr.png')

    def make_points_graphic(self, data_list, pattern):
        plt.clf()
        if pattern == 'best' or pattern == 'worst':
            keys_list = self.extreme_keys
        else:
            keys_list = self.all_keys
        for key in keys_list:
            plt.clf()
            for data in data_list:
                xs = []
                ys = []
                ints = []
                for x in data[key].points:
                    xs.append(x)
                    ys.append(data[key].points[x].y)
                    ints.append(data[key].points[x].int)
                plt.plot(xs, ys, 'ro', color=data[key].color)
                for i in range(len(xs)):
                    plt.plot((xs[i], xs[i]),
                             (ys[i]-ints[i], ys[i]+ints[i]),
                             color='black')
            # plt.xlabel('Размер данных')
            # plt.ylabel('Время обработки')
            # plt.show()
            plt.savefig(pattern + '_' + key + '_points.png')

    def make_memory_diagramm(self, data_dict):
        names_dict = {ArraysWithLinearSearch: 'lin',
                      BinarySearchArrays: 'bin',
                      SimpleTreeDict: 'tree',
                      AVLTreeDict: 'avl',
                      HashTableDict: 'hash'}
        plt.clf()
        names = ['lin', 'bin', 'tree', 'avl', 'hash']
        values = []
        for i in range(len(names)):
            for key in data_dict:
                if names_dict[key] == names[i]:
                    values.append(data_dict[key])
        xs = range(len(names))
        plt.bar([x for x in xs], [value for value in values], color='blue')
        plt.xticks(xs, names)
        # plt.show()
        plt.savefig('memory_diagramm.png')
