__author__ = "Roman Wang"

import math
import scipy.constants as constants
from decimal import *

# Fibonacci as sum of two geometric series - can be solved for by solving associated homogenous recurrence relation
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return round((constants.golden**n-constants.golden**(-n))/math.sqrt(5))

# Notice all even fibonacci numbers are 3 apart from the properties of adding odd/even numbers
# We can produce a solution that is constant instead of O(n) and (n^2) by using the solved fib equation and algebraic manipulation
def fib_even(n):
    phi = constants.golden
    psi = 1-phi

    geom_phi = phi**3 * (1-phi**(3*n))/(1-phi**3)
    geom_psi = psi**3 * (1-psi**(3*n))/(1-psi**3)
    return round((geom_phi-geom_psi)/(math.sqrt(5)))

if __name__ == "__main__":
    print(constants.golden)
    print(fib(33), fib(34))
    print(fib_even(33//3))
