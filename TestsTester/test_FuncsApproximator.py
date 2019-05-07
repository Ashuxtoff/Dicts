import os
import sys
import unittest
import math
from collections import namedtuple
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))
from Tester.FuncsApproximator import FuncsApproximator


class TestApproximator(unittest.TestCase):
    def setUp(self):
        e = math.e
        self.approximator = FuncsApproximator()
        test_data = namedtuple('data', 'points')
        y = namedtuple('y', 'y')
        self.lin_data = {-1: 0, 0: 0.5, 1: 1, 3: 2, 5: 3, 7: 4}
        self.log_data = test_data({e: y(2), e**2: y(3), e**3: y(4),
                                   e**4: y(5), e**5: y(6)})
        self.pow_data = test_data({1: y(2), 2: y(16), 3: y(54),
                                   4: y(128), 5: y(250)})

    def test_lin_approximation(self):
        self.assertEqual((0.5, 0.5),
                         self.approximator.lin_approximate(self.lin_data))

    def test_log_approximation(self):
        self.assertEqual((1, 1),
                         self.approximator.log_approximate(self.log_data))

    def test_pow_approximation(self):
        self.assertGreater(self.approximator.pow_approximate(
            self.pow_data)[0] + 0.1, 1)
        self.assertGreater(self.approximator.pow_approximate(
            self.pow_data)[1] + 0.1, 3)


if __name__ == '__main__':
    unittest.main()
