# tests/test_calculator.py

import pytest
from src.calculator import prepare, calculate

class TestCalculator:
    VALID_EXPRESSIONS = [
        ("2 + 3", (2.0, '+', 3.0)),
        ("5 - 2", (5.0, '-', 2.0)),
        ("4 * 5", (4.0, '*', 5.0)),
        ("10 / 2", (10.0, '/', 2.0)),
    ]

    INVALID_EXPRESSIONS = [
        ("2 +", None),
        ("a + b", None),
    ]

    VALID_CALCULATIONS = [
        (2.0, '+', 3.0, 5.0),
        (5.0, '-', 2.0, 3.0),
        (4.0, '*', 5.0, 20.0),
        (10.0, '/', 2.0, 5.0),
    ]

    @pytest.mark.parametrize("expression, expected", VALID_EXPRESSIONS)
    def test_prepare_valid_expression(self, expression, expected):
        result = prepare(expression)
        assert result == expected, f"Ожидаемый результат: {expected}, полученный результат: {result}"

    @pytest.mark.parametrize("expression, expected", INVALID_EXPRESSIONS)
    def test_prepare_invalid_expression(self, expression, expected):
        result = prepare(expression)
        assert result == expected, f"Ожидаемый результат: {expected}, полученный результат: {result}"

    @pytest.mark.parametrize("one, action, two, expected", VALID_CALCULATIONS)
    def test_calculate_valid_expression(self, one, action, two, expected):
        result = calculate(one, action, two)
        assert result == expected, f"Ожидаемый результат: {expected}, полученный результат: {result}"