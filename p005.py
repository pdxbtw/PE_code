# Project Euler - Problem 5
# -----------------------------------------------------------------------------
# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder. What is the smallest positive number
# this is evenly divisible by all of the numbers from 1 to 20?

import time

# Simply list the prime factors for integers from 1 - 20
# There will be multiple 2s and 3s to accomodate 20, 16, 12, 8, 4, 18, and 9

start = time.time()
a = 19*17*13*11*7*5*3*2*2*2*2*3
stop = time.time()
print(a)
print('Time: {} seconds'.format(stop - start))
