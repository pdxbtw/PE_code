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

# from decimal import *
# exec(open("V:/sandbox_wilson_b/PE/PE_022.py").read()) 

import time
import math
start = time.time()

i_min = 12
i_max = 28123
abund = []
for i in range(i_min, i_max+1, 1):
        divsum = 1
        f_max = math.floor(math.sqrt(i))
        fact = 1
        while fact < f_max:
                fact += 1
                if i % fact == 0:
                        f_low = fact
                        f_high = i/fact
                        if f_low == f_high: # repeated factors
                                f_high = 0
                        divsum += f_low + f_high
        if divsum > i:
                abund += [i,]

n = len(abund)
raw = [i for i in range(i_max + 1)]
for i in range(n, 0, -1):
        high = i-1
        low = 0
        test = 0
        while high >= low:
                test = abund[high] + abund[low]
                if test > i_max:
                        break
                if test in raw:
                        raw.remove(test)
                low += 1
end = time.time()
print(sum(raw))
print(len(raw))
print('Processing Time: {} seconds'.format(end-start))
# Answer: 4179871
# Time: 3.21E+3 seconds

