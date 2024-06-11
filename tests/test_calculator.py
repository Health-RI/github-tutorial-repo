# SPDX-FileCopyrightText: 2024 Stichting Health-RI
#
# SPDX-License-Identifier: apache-2.0

from simple_calculator.calculator import Calculator


def test_add():
    calculator = Calculator()
    assert calculator.add(3, 7) == 10

def test_subtract():
    calculator = Calculator()
    assert calculator.subtract(1, 7) == -6

def test_multiply():
    calculator = Calculator()
    assert calculator.multiply(7, 7) == 49

def test_divide():
    calculator = Calculator()
    assert calculator.divide(49, 7) == 7
