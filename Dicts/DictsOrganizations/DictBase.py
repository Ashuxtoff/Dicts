class DictBase(object):
    def contains(self, key):
        raise NotImplementedError()

    def clear(self):
        raise NotImplementedError()

    def fromkeys(self, sequence, value=None):
        raise NotImplementedError()

    def get(self, key, default=None):
        raise NotImplementedError()

    def items(self):
        raise NotImplementedError()

    def keys(self):
        raise NotImplementedError()

    def setdefault(self, key, value=None):
        raise NotImplementedError()

    def update(self, other):  # **kwargs?
        raise NotImplementedError()

    def popitem(self):
        raise NotImplementedError()

    def pop(self, key, value=None):
        raise NotImplementedError()

    def values(self):
        raise NotImplementedError()

    def copy(self):
        raise NotImplementedError()

    def __delitem__(self, item):
        raise NotImplementedError()

    def __eq__(self, other):
        raise NotImplementedError()

    def __iter__(self):
        raise NotImplementedError()

    def __len__(self):
        raise NotImplementedError()
