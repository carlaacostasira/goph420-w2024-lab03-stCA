import unittest
import numpy as np
import matplotlib.pyplot as plt
from goph420_lab03.regression import multi_regress

class TestMultiRegression(unittest.TestCase):
    def setUp(self):
        self.y = range(0,20, 2)
        self.z = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 4, 2, 6, 8, 3, 8, 9, 10, 14]
        
        regression = multi_regress(self.y, self.z)
        
if __name__ == '__main__':
    unittest.main()
        