# Project Euler - Problem 7
# -----------------------------------------------------------------------------
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13. What is the 10001st prime number?

import math
import time


def primeSieve(numPrime, rtrnList=False):
    primeList = [None] * numPrime
    primeList[0] = 2
    testVal = 1
    index = 1
    while index < numPrime:
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

    if not rtrnList:
        return primeList[-1]
    else:
        return primeList


start = time.time()
val = primeSieve(10001, rtrnList=False)
stop = time.time()
print(val)
print('Time: {} seconds'.format(stop-start))
