# Project Euler - Problem 1
# ----------------------------------------------------------------------------- 
# If we list all the natrual numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6, and 9. The sum of these multiples is 23. Find the sum of all
# the multiples of 3 or 5 below 1000.

import time
import math


# OPTION 1: Loop with conditional statements
def fizzBuzzLoop(top_limit):
    total = 0
    count = 1
    while count < top_limit:
        if not count % 3:
            total += count
        elif not count % 5:
            total += count
        count += 1
    return total


start = time.time()
total = fizzBuzzLoop(1000)
stop = time.time()
print(total)
print('OPTION 1: Time = {} seconds'.format(stop - start))


# OPTION 2: Direct calculation
# using the following identities:
#   The union of A and B = A + B - (A intersection B)
#   and sum of natural numbers (n) = n*(n+1)/2
# we can directly find a result
def fizzBuzzDirect(top_limit):
    i = math.floor(top_limit/3)
    j = math.floor(top_limit/5)
    k = math.floor(top_limit/15)
    return int((3*i*(i+1) + 5*j*(j+1) - 15*k*(k+1))*0.5)


start = time.time()
val = 1000 - 0.1
total = fizzBuzzDirect(val)
stop = time.time()
print(total)
print('OPTION 2: Time = {} seconds'.format(stop - start))
