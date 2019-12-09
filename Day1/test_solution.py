"""
Tests for day 1
"""
import pytest

from solution import (
    calculate_fuel,
    get_input,
    solve_first_part,
    solve_second_part,
    calculate_total_fuel,
)


def test_get_input_returns_list():
    """
    Verify that function returns a list object
    """
    output = type(get_input("input.txt"))
    expected = list
    assert output == expected, "Expected list as output"


def test_get_input_returns_list_of_ints():
    """
    Get input should return a list of ints
    """
    output = all(isinstance(input_line, int) for input_line in get_input("input.txt"))
    expected = True
    error = f"Expected all lines from file to be int"
    assert output == expected, error


def test_calculate_fuel_given_12():
    """
    Verify fuel calculation works
    """
    output = calculate_fuel(12)
    expected = 2
    error = f"Expected {expected}, got {output}"
    assert output == expected, error


def test_calculate_fuel_floors():
    """
    Verify fuel calculation works
    """
    output = calculate_fuel(14)
    expected = 2
    error = f"Expected {expected}, got {output}"
    assert output == expected, error


def test_calculate_fuel_1969():
    """
    Verify fuel calculation works
    """
    output = calculate_fuel(1969)
    expected = 654
    error = f"Expected {expected}, got {output}"
    assert output == expected, error


def test_calculate_fuel_100756():
    """
    Verify fuel calculation works
    """
    output = calculate_fuel(100756)
    expected = 33583
    error = f"Expected {expected}, got {output}"
    assert output == expected, error


def test_calculate_fuel_returns_0_when_negative():
    """
    Verify fuel calculation works
    """
    output = calculate_fuel(2)
    expected = 0
    error = f"Expected {expected}, got {output}"
    assert output == expected, error


def test_solve_first_part():
    """
    Verify first solution function with test data
    """
    puzzle_input = [1969, 12, 14, 100756]
    output = solve_first_part(puzzle_input)
    expected = 654 + 2 + 2 + 33583
    error = f"Expected {expected}, got {output}"
    assert output == expected, error


def test_calculate_total_fuel_14():
    """
    Verify total fuel calculation
    """
    output = calculate_total_fuel(14)
    expected = 2
    error = f"Expected {expected}, got {output}"
    assert output == expected, error


def test_solve_second_part_14():
    """
    Verify first solution function with test data
    """
    puzzle_input = [14]
    output = solve_second_part(puzzle_input)
    expected = 2
    error = f"Expected {expected}, got {output}"
    assert output == expected, error


def test_solve_second_part_1969():
    """
    Verify first solution function with test data
    """
    puzzle_input = [1969]
    output = solve_second_part(puzzle_input)
    expected = 654 + 216 + 70 + 21 + 5
    error = f"Expected {expected}, got {output}"
    assert output == expected, error


def test_solve_second_part_100756():
    """
    Verify first solution function with test data
    """
    puzzle_input = [100756]
    output = solve_second_part(puzzle_input)
    expected = 50346
    error = f"Expected {expected}, got {output}"
    assert output == expected, error


if __name__ == "__main__":
    pytest.main()
