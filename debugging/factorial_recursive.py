#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function to compute the factorial of a number recursively.

    Parameters:
        n (int): The number for which factorial is to be computed.

    Returns:
        int: The factorial of the given number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Check if the correct number of command line arguments is provided
if len(sys.argv) != 2:
    print("Usage: python script_name.py <number>")
    sys.exit(1)

try:
    # Get the number from command line argument and compute its factorial
    f = factorial(int(sys.argv[1]))
    print(f)
except ValueError:
    print("Error: Please provide a valid integer.")
    sys.exit(1)
