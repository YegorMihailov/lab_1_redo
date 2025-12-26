import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.calculator import *


class TestCalculator(unittest.TestCase):
    """Tests for calculator"""

    def test_arithmetic_operations(self):
        self.assertEqual(evaluate(' 2.5 + 3 / 0.5 * 5'), 32.5)
    
    def test_unary(self):
        self.assertEqual(evaluate('2 + -3 * -5 / -1'), -13)
    
    def test_one_number(self):
        self.assertEqual(evaluate('5'), 5)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            evaluate('5 / 0')
    
    def test_unknown_symbol(self):
        with self.assertRaises(ValueError):
            evaluate('R / 5')
    
    def test_invalid_expression(self):
        self.assertEqual(evaluate('+'), 'Invalid expression')
        self.assertEqual(evaluate('5-*5'), 'Invalid expression')
        self.assertEqual(evaluate('5/*5'), 'Invalid expression')
        self.assertEqual(evaluate('5-*-5'), 'Invalid expression')
        self.assertEqual(evaluate('5+'), 'Invalid expression')
        self.assertEqual(evaluate('/5'), 'Invalid expression')
        

    