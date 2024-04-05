import unittest
import numpy as np
import matplotlib.pyplot as plt
from goph420_lab03.regression import multi_regress

class TestMultiRegression1(unittest.TestCase):
    def setUp(self):
        self.z = np.array([0, 2.3, 4.9, 9.1, 13.7, 18.3, 22.9, 27.2])
        self.y = np.array([22.8, 22.8, 22.8, 20.6, 13.9, 11.7, 11.1, 11.1])
        
    def test_multi_regress(self):
        expected_output_coeffs = np.array([23.7155, -0.5378])
        expected_output_r2 = 0.90087
        
        actual_output_coeff = (multi_regress(self.y, self.z)[0])
        actual_output_r2 = round(multi_regress(self.y, self.z)[2], 5)
        
        np.testing.assert_almost_equal(expected_output_coeffs, actual_output_coeff, 4)
        np.testing.assert_almost_equal(expected_output_r2, actual_output_r2)


if __name__ == '__main__':
    unittest.main()