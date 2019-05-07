class CurrentData:
    def __init__(self, input_dict):
        self.data_dict = {"clear": 0, "contains": 0, "fromkeys": 0,
                          "copy": 0, "get": 0, "items": 0, "keys": 0,
                          "pop": 0, "popitem": 0, "setdefault": 0,
                          "update": 0, "values": 0}
        if len(input_dict) > 0:
            self.data_dict.update(input_dict)

    def __add__(self, other):
        for key in self.data_dict:
            self.data_dict[key] += other.data_dict[key]
        return self

    def __truediv__(self, n):
        for key in self.data_dict:
            self.data_dict[key] /= n
        return self

    def __sub__(self, other):
        return self.__add__(other/(-1))

    def __iadd__(self, other):
        return self.__add__(other)

    def __itruediv__(self, n):
        return self.__truediv__(n)

    def __eq__(self, other):
        for key in self.data_dict:
            if self.data_dict[key] != other.data_dict[key]:
                return False
        return True


class CurrentTypeStorage:
    def __init__(self, random_data, worst_data, best_data):
        self.random = random_data
        self.worst = worst_data
        self.best = best_data
        self.current_data_list = [self.random, self.worst, self.best]

    def __add__(self, other):
        self.random += other.random
        self.worst += other.worst
        self.best += other.best
        return self

    def __truediv__(self, n):
        for data in self.current_data_list:
            data /= n
        return self

    def __sub__(self, other):
        return self.__add__(other/(-1))

    def __iadd__(self, other):
        return self.__add__(other)

    def __itruediv__(self, n):
        return self.__truediv__(n)

    def __eq__(self, other):
        return self.random == other.randoAm and \
               self.best == other.best and \
               self.worst == other.worst


class DataStorage:
    def __init__(self, lin_data, bin_data, tree_data, avl_data, hash_data):
        self.lin_data = lin_data
        self.bin_data = bin_data
        self.tree_data = tree_data
        self.avl_data = avl_data
        self.hash_data = hash_data
        self.data_list = [self.lin_data, self.bin_data,
                          self.tree_data, self.avl_data,
                          self.hash_data]

    def __add__(self, other):
        self.lin_data += other.lin_data
        self.bin_data += other.bin_data
        self.tree_data += other.tree_data
        self.avl_data += other.avl_data
        self.hash_data += other.hash_data
        return self

    def __truediv__(self, n):
        for data in self.data_list:
            data /= n
        return self

    def __sub__(self, other):
        return self.__add__(other/(-1))

    def __iadd__(self, other):
        return self.__add__(other)

    def __itruediv__(self, n):
        return self.__truediv__(n)

    def __eq__(self, other):
        return self.bin_data == other.bin_data and \
               self.lin_data == other.lin_data and \
               self.avl_data == other.avl_data and \
               self.tree_data == other.tree_data and \
               self.hash_data == other.hash_data
