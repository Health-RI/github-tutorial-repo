# SPDX-FileCopyrightText: 2024 Stichting Health-RI
#
# SPDX-License-Identifier: apache-2.0

from simple_calculator.calculator import Calculator


def test_add():
    calculator = Calculator()
    assert calculator.add(3, 7) == 10
