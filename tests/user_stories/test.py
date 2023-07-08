"""
USER STORY TESTS: 3, 8

"""
import unittest
import os
import sys
import numpy as np

root_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(root_dir))

sys.path.append(f"{parent_dir}/src")

from src.user_stories import plot_weather_parameters_annual
from src.user_stories import linear_regression


class TestUserStories(unittest.TestCase):
    def test_plot_weather_parameters_annual_one(self):
        print("\n Testing user story 3 [1/2]")
        with self.assertRaises(AssertionError):
            plot_weather_parameters_annual([1923, 1925, 1924])

    def test_plot_weather_parameters_annual_two(self):
        print("\n Testing user story 3 [2/2]")
        # Additional test case with sorted years
        plot_weather_parameters_annual([1981, 1982, 1983])

    def test_linear_regression_one(self):
        print("\n Testing user story 8 [1/2]")
        x_data = np.asarray([2, 3, 4])
        y_data = np.asarray([7, 9, 11])
        result = linear_regression(x_data, y_data, 7)
        self.assertEqual(result, 17.0)

    def test_linear_regression_two(self):
        print("\n Testing user story 8 [2/2]")
        x_data = np.empty(2)
        y_data = np.empty(3)
        with self.assertRaises(AssertionError):
            linear_regression(x_data, y_data, 1)


if __name__ == '__main__':
    unittest.main()
