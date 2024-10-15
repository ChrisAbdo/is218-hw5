"""
This module contains unit tests for the Calculation class.
"""

from decimal import Decimal
import pytest
from app.calculator.calculation import Calculation
from app.calculator.operations import add, subtract, multiply, divide


def test_ops(a, b, operation, expected):
    """
    Test the Calculation class with the add, subtract, multiply, and divide operations.
    """
    calc = Calculation(Decimal(str(a)), Decimal(str(b)), operation)
    assert calc.execute_calculation() == Decimal(str(expected)), f"Failed {operation.__name__}"

def test_divide_by_zero():
    """
    Test that dividing by zero raises a ZeroDivisionError.
    """
    calc = Calculation(Decimal('10'), Decimal('0'), divide)
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        calc.execute_calculation()