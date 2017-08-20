# Project Euler - Problem 9
# -----------------------------------------------------------------------------
# A Pythagorean triplet is a set of three natural numbers, a<b<c, for which
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000
# Find the product of a*b*c.

import time


def pythagoreanTriplet(tripleSum):
    a = 1
    b = 2
    c = tripleSum - a - b
    while a < c+1:
        while b < c:
            if (a**2 + b**2) == c**2:
                return (a*b*c)
            c -= 1
            b += 1
        a += 1
        b = a + 1
        c = tripleSum - a - b


start = time.time()
print(pythagoreanTriplet(1000))
stop = time.time()
print('Time: {} seconds'.format(stop-start))
