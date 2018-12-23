__author__ = "Roman Wang"
import scipy.constants as constants
import math

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
    pass

if __name__ == "__main__":
    print(constants.golden)
    print(fib(6))
