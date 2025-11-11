"""
Title: Fermat's Last Theorem — Near Miss Finder
File: fermat_near_miss.py
External files required: None
External files created: None
Programmers: Manoj Reddy (manoj@example.com), Partner Name (partner@example.com)
Course & Section: CPSC XXX - Software Engineering, Section Y
Completion / Submission Date: November XX, 2025
Description:
    Interactive program that searches for integer "near misses" of Fermat's equation:
        x^n + y^n ~= z^n
    The user supplies n (3 <= n <= 11) and k (k > 10). For each pair (x, y) with
    10 <= x <= k and 10 <= y <= k the program computes which integer z or z+1
    is closest to x^n + y^n, records the miss (absolute difference) and the
    relative miss (miss / (x^n + y^n)). Every time a new smallest relative miss
    is found, it is printed. The final (smallest) miss is printed last.
Resources used:
    - Python 3.11 documentation (math, pow)
    - Assignment specification provided by instructor
Language & Version: Python 3.x (tested with 3.10/3.11)
How to run (brief):
    - Ensure Python 3.x is installed.
    - Run: python fermat_near_miss.py
    - Or use provided run script / create exe per README.
"""

import math
import sys

def prompt_int(prompt, validate_fn, err_msg):
    """
    Prompt repeatedly until user gives a valid integer that passes validate_fn.
    validate_fn: function(int) -> bool
    err_msg: message to show on invalid input
    """
    while True:
        val = input(prompt).strip()
        if val == "":
            print("Input cannot be blank. Please enter an integer.")
            continue
        try:
            ival = int(val)
        except ValueError:
            print("Please enter a valid integer.")
            continue
        if not validate_fn(ival):
            print(err_msg)
            continue
        return ival

def compute_best_near_miss(n, k):
    """
    Search (x, y) pairs for the smallest relative miss.
    Returns a dict with best_x, best_y, best_z, actual_miss, relative_miss.
    """
    # Track smallest found relative miss
    smallest_relative = float('inf')
    best = {'x': None, 'y': None, 'z': None, 'actual_miss': None, 'relative_miss': None}

    # Loop over x, y pairs
    # We loop y from x to k to avoid symmetric duplicates (x,y) and (y,x)
    for x in range(10, k + 1):
        # loop purpose: iterate candidate y values to test combinations with current x
        for y in range(x, k + 1):
            lhs = pow(x, n) + pow(y, n)  # integer pow works for big integers in Python

            # Estimate z as the integer floor of the nth root of lhs
            z = int(lhs ** (1.0 / n))

            # Evaluate z and z+1 as bracket candidates
            z_pow = pow(z, n)
            z1_pow = pow(z + 1, n)

            # Compute misses (non-negative)
            miss1 = abs(lhs - z_pow)
            miss2 = abs(z1_pow - lhs)

            # Pick smaller miss and determine which z gives it
            if miss1 <= miss2:
                actual_miss = miss1
                chosen_z = z
            else:
                actual_miss = miss2
                chosen_z = z + 1

            # Relative miss
            # lhs is non-zero because x,y >= 10 and n>=3
            relative_miss = actual_miss / lhs

            # If this is a new smallest, print and update
            if relative_miss < smallest_relative:
                smallest_relative = relative_miss
                best.update({
                    'x': x, 'y': y, 'z': chosen_z,
                    'actual_miss': actual_miss, 'relative_miss': relative_miss
                })
                # Print a clear, labeled update
                print("\n--- New best near miss found ---")
                print(f"x = {x}, y = {y}, chosen z = {chosen_z}")
                print(f"Actual miss (integer) = {actual_miss}")
                # Show both fraction and percent to satisfy UX requirement
                print(f"Relative miss = {relative_miss:.10f} ({relative_miss * 100:.6f}%)")

    return best

def main():
    print("Fermat Near Miss Finder")
    print("Find integer near-misses of x^n + y^n ≈ z^n")
    print("Note: valid n values are integers with 3 ≤ n ≤ 11. x and y range from 10..k (k>10).")
    # Prompt for n with validation
    n = prompt_int(
        "Enter exponent n (integer, 3..11): ",
        lambda v: 3 <= v <= 11,
        "Invalid. n must be an integer between 3 and 11 (inclusive)."
    )

    # Prompt for k with validation
    k = prompt_int(
        "Enter upper bound k for x and y (integer, k > 10): ",
        lambda v: v > 10,
        "Invalid. k must be an integer greater than 10."
    )

    print(f"\nSearching near misses with n = {n}, x and y in [10, {k}] ...")
    print("This may take a while for large k. The program will report each time a new best is found.\n")

    try:
        best = compute_best_near_miss(n, k)
    except KeyboardInterrupt:
        print("\nSearch interrupted by user. Showing best found so far...\n")
        # If keyboard interrupt, fall through to best if available
        best = best if 'best' in locals() else {'x':None, 'y':None, 'z':None, 'actual_miss':None, 'relative_miss':None}

    # Final result printed last, clearly labeled
    print("\n=== FINAL / BEST RESULT (printed last) ===")
    if best['x'] is not None:
        print(f"x = {best['x']}, y = {best['y']}, z = {best['z']}")
        print(f"Actual miss = {best['actual_miss']}")
        rm = best['relative_miss']
        print(f"Relative miss = {rm:.12f} ({rm * 100:.8f}%)")
    else:
        print("No valid results found.")

    # Pause to allow review
    input("\nPress Enter to exit and allow you to review the output...")

if __name__ == "__main__":
    main()
