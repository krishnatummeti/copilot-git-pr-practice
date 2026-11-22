# Path: GitHub-Copolot/copilot-git-pr-practice/test_calculator.py
# pytest is a testing framework for Python. It allows you to write test cases for your code and run them to ensure that your code behaves as expected. In this file, we will write unit tests for the calculator module.
# python version: 3.8
import unittest
# Import the functions to be tested from the calculator module
from calculator import add, divide

# This is a test file for the calculator module. It contains unit tests for the add and divide functions.
class CalculatorTests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaisesRegex(ValueError, "Cannot divide by zero"):
            divide(10, 0)

# Run the tests if this file is executed directly
if __name__ == "__main__":
    unittest.main()