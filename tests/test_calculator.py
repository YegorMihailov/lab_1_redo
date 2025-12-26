import unittest
import sys
import os
from src.calculator import *

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


class TestCalculator(unittest.TestCase):
    """Tests for calculator"""

    def test_arithmetic_operations(self):
        """Tests expression with arithmetic operations and float numbers"""

        self.assertEqual(evaluate('2.5 + 3 / 0.5 * 5'), 32.5)
    
    def test_unary(self):
        """Tests expression with arithmetic operations with unary"""

        self.assertEqual(evaluate('2 + -3 * -5 / -1'), -13)
    
    def test_one_number(self):
        """Tests expression with one number"""

        self.assertEqual(evaluate('5'), 5)

    def test_division_by_zero(self):
        """Tests division by zero"""

        with self.assertRaises(ZeroDivisionError):
            evaluate('5 / 0')
    
    def test_unknown_symbol(self):
        """Tests expression with unknown symbol"""

        with self.assertRaises(ValueError):
            evaluate('R / 5')
    
    def test_invalid_expression(self):
        """Tests invalid expression"""

        self.assertEqual(evaluate('+'), 'Invalid expression')
        self.assertEqual(evaluate('5-*5'), 'Invalid expression')
        self.assertEqual(evaluate('5/*5'), 'Invalid expression')
        self.assertEqual(evaluate('5-*-5'), 'Invalid expression')
        self.assertEqual(evaluate('5+'), 'Invalid expression')
        self.assertEqual(evaluate('/5'), 'Invalid expression')
        

    