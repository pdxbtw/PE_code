# Project Euler - Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13. What is the 10001st prime number?

from decimal import *
import math
import time
getcontext().prec = 3
start = time.clock()

nprime = 10001
primes = (2,)
test_val = 3
isprime = True
run = True
while run:
    stop = math.floor(math.sqrt(test_val))
    for i in range(len(primes)):
        if primes[i] > stop:
            break
        
        if test_val % primes[i] == 0:
            isprime = False
            break
        else:
            isprime = True

    if isprime:
        primes += (test_val,)
        if len(primes) == nprime:
            run = False
    test_val += 2
end = time.clock()
print(primes[-1])
print('Processing Time:', Decimal(end) - Decimal(start), 'seconds')
 
