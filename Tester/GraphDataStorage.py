from collections import namedtuple


class CurrentData:
    def __init__(self, appr_type, color):
        self.points = {}
        self.appr_type = appr_type
        self.color = color
        self.yi = namedtuple('yi', 'y int')

    def append(self, x, y, interval):
        self.points[x] = self.yi(y, interval)
