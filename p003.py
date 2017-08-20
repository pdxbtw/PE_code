# Project Euler - Problem 3
# -----------------------------------------------------------------------------
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
import time


def biggestPrimeFact(value):
    max_prime = None        # Initializing max_prime factor
    while value % 2 == 0:   # Check if even
        value = value / 2
        max_prime = 2

    count = 3
    while count <= value:   # Check odd factors
        if not value % count:
            value = value / count
            max_prime = count
        else:
            count += 2
    return max_prime


start = time.time()
max_prime = biggestPrimeFact(600851475143)
stop = time.time()
print(max_prime)
print('Time: {} seconds'.format(stop - start))
