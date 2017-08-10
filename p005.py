# Project Euler - Problem 5
# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder. What is the smallest positive number
# this is evenly divisible by all of the numbers from 1 to 20?

import time
start = time.time()

a = 19*17*13*11*7*5*3*2*2*2*2*3
end = time.time()
print(a)
print('Processing Time: {} seconds'.format(end-start))
