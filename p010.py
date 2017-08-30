# Project Euler - Problem 10
# -----------------------------------------------------------------------------
# The sum of the primes below 10 is 2+3+5+7 = 17.
# Find the sum of all primes below two million.

import math
import time


def primeSieve(bound):
    aproxPrimes = bound / (math.log(bound) - 1.08366)   # Prime number theorem
    primeList = [0] * math.floor(aproxPrimes)
    primeList[0] = 2
    testVal = 1
    index = 1
    while testVal <= bound:
        testVal += 2
        prime = True
        searchStop = math.sqrt(testVal)
        for i in primeList:
            if i > searchStop:
                break
            if not testVal % i:
                prime = False
                break
        if prime:
            primeList[index] = testVal
            index += 1
    return sum(primeList)


start = time.time()
primeSum = primeSieve(2000000)
stop = time.time()
print(primeSum)
print('Time: {} seconds'.format(stop-start))
