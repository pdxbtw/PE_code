# Project Euler - Problem 23
# -----------------------------------------------------------------------------
# A perfect number is a number for which the sum of its proper divisors is
# exactly equal to the number. For example, the sum of the proper divisors of
# 28 would be 1+2+4+7+14=28, which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than
# n and it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1+2+3+4+6=16, the smallest number that
# can be written as the sum of two abundant numbers is 24. By mathematical
# analysis, it can be shown that all integers greater than 28123 can be written
# as the sum of two abundant numbers. However, this upper limit cannot be
# reduced any further by analysis even though it is known that the greatest
# number that cannot be expressed as the sum of two abundant numbers is less
# than this limit.
#
# Find the sum of all positive integers which cannot be written as the sum of
# two abundant numbers.

import time
import math


def genAbundList(bound):
    nmin = 12
    nmax = bound - nmin
    abund = []
    for i in range(nmin, nmax+1):
        divsum = 1
        fact = 2
        f_max = math.sqrt(i)
        while fact <= f_max:
            if not i % fact:
                f_low = fact
                f_high = i // fact
                if f_low == f_high:  # repeated factors
                    f_high = 0
                divsum += f_low + f_high
            fact += 1
        if divsum > i:
            abund.append(i)
    return abund


def findAbundSums(abundList, bound):
    abundSum = [j+i for j in abundList for i in abundList if j+i <= bound]
    abundSum = sum(set(abundSum))
    n = (bound * (bound + 1) // 2) - abundSum
    return n

start = time.time()
bound = 28123 
abund = genAbundList(bound)
n = findAbundSums(abund, bound)
stop = time.time()
print(n)
print('Time: {} seconds'.format(stop-start))
# Answer: 4179871
# Time: 3.21E+3 seconds
