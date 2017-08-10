# Project Euler - Problem 10
# The sum of the primes below 10 is 2+3+5+7 = 17.
# Find the sum of all primes below two million.

import math
import time
start = time.time()

stop_val = 2e6
primes = (2,)
test_val = 3
isprime = True
run = True
while test_val < stop_val:
    stop = math.floor(math.sqrt(test_val))
    isprime = True
    for i in range(len(primes) + 1):
        if primes[i] > stop:
            break
        
        if test_val % primes[i + 1] == 0:
            isprime = False
            break

    if isprime:
        primes += (test_val,)
    test_val += 2

end = time.time()
print(sum(primes))
print('Processing Time: {} seconds'.format(end-start))
