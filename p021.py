# Project Euler - Problem 21
# -----------------------------------------------------------------------------
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n
# which divide evenly into n). If d(a) = b and d(b) = a, where a!=b, then a and
# b are an amicable pair and each of a and b are called amicable numbers.
# Evaluate the sum of all the amicable numbers under 10,000

import time
import math


def genPropDiv(bound):
    # Generate dictionary with int keys 3x the bound
    d = {}
    for i in range(3*bound):
        d[i] = 0

    # Compute divisor sums from 2 up to the bound
    for i in range(2, bound+1, 1):
        # pdb.set_trace()
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
        d[i] = divsum   # Update dictionary
    return d


def amicableNumSearch(d):
    amic_sum = 0
    perf_sum = 0
    for i in d:
        if d[d[i]] == i:    # Find amicable or perfect numbers
            amic_sum += i
            if d[i] == i:   # Find perfect numbers
                perf_sum += i
    return amic_sum - perf_sum  # Remove perfect numbers from sum


start = time.time()
bound = 10000
a = genPropDiv(bound)
amic_sum = amicableNumSearch(a)
stop = time.time()
print(amic_sum)
print('Time: {} seconds'.format(stop-start))
