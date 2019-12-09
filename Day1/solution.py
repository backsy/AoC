"""
Day1 part1 solution code
"""

from math import floor


def main():
    """
    Main function that calculates solutions for given days puzzles
    """
    input_file = "input.txt"
    puzzle_input = get_input(input_file)
    solution_part_1 = solve_first_part(list(puzzle_input))
    print(f"Solution 1: {solution_part_1}")
    solution_part_2 = solve_second_part(list(puzzle_input))
    print(f"Solution 2: {solution_part_2}")


def solve_first_part(puzzle_input):
    """
    Solves the first part of the puzzle
    """
    return sum(calculate_fuel(mass) for mass in puzzle_input)


def solve_second_part(puzzle_input):
    """
    Solves the second part of the puzzle
    """
    return sum(calculate_total_fuel(mass) for mass in puzzle_input)


def calculate_total_fuel(mass):
    """
    Calculates the fuel needed to lift the mass and fuel
    """
    fuel_needed = 0
    mass_to_carry = mass
    while mass_to_carry:
        mass_to_carry = calculate_fuel(mass_to_carry)
        fuel_needed += mass_to_carry
    return fuel_needed


def get_input(input_filename):
    """
    Load file into a list and strip newline chars
    """
    output = []
    with open(input_filename) as input_file:
        for line in input_file:
            output.append(int(line.replace("\n", "")))
    return output


def calculate_fuel(mass):
    """
    Calculate the fuel needed for lifting given mass
    """
    fuel_mass = floor(mass / 3) - 2
    if fuel_mass < 0:
        return 0
    return fuel_mass


if __name__ == "__main__":
    main()
