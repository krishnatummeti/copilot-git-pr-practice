import unittest

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