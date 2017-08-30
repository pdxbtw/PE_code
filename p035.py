# Project Euler - Problem 35
# -----------------------------------------------------------------------------
# The number, 197, is called a circular prime because all rotations of the
# digits: 197, 971, and 719, are themselves prime. There are 13 such primes
# below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97. How many
# circular primes are there below one million?

import math
import time
# import pdb
# pdb.set_trace()


def prime_sieve(bound):
    aproxPrimes = bound / (math.log(bound) - 1.08366)   # Prime number theorem
    primeList = [0] * math.floor(aproxPrimes)
    primeList[0] = 2
    testVal = 3
    index = 1
    while testVal <= bound:
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
        testVal += 2
    return primeList[0:index]


def circ_primes(primes):
    circ_prime = {1: 2, 2: 5}
    count = 2
    for p in primes:
        c_prime = True
        str_p = str(p)
        if (
                '0' in str_p or '2' in str_p or
                '4' in str_p or '5' in str_p or
                '6' in str_p or '8' in str_p):
            continue
        for n in str_p:
            str_p = str_p[1:] + str_p[0]
            if int(str_p) not in primes:
                c_prime = False
                break
        if c_prime:
            count += 1
            circ_prime[count] = p
    return len(circ_prime)


start = time.time()
bound = 999999
primes = prime_sieve(bound)
ans = circ_primes(primes)
stop = time.time()
print(ans)
print("Time: {} seconds".format(stop-start))
