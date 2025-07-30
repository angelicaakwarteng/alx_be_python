import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        # Add more assertions to thoroughly test the add method.
    
    def test_subtraction(self):
        """Test the subtraction method"""
        self.assertEqual(self.calc.subtract(10, 2), 8)
        self.assertEqual(self.calc.subtract(-10, -10), 0)

    def test_multiplication(self):
        """Test the subtraction method"""
        self.assertEqual(self.calc.multiply(10, 2), 20)
        self.assertEqual(self.calc.multiply(-10, -10), 100)

    def test_division(self):
        """Test the subtraction method"""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(10, 0), None)