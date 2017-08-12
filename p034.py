#!/home/fure_j/Software/pypy3-2.4-linux_x86_64-portable/bin/pypy 
# !/home/wilson_b/anaconda3/bin/python

# Project Euler - Problem 34
# -----------------------------------------------------------------------------
# 145 is a curious number, as 1! + 4! + 5! = 145. Find the sum of all numbers 
# which are equal to the sum of the factorial of their digits.
# Note: as 1! and 2! are not sums, they are not included.

from decimal import *
import time
import pdb
import math
getcontext().prec = 3
#pdb.set_trace()
start = time.clock()

sum_t = 0
count = 10
while count < 1e7:
        num_s = str(count)
        sum = 0
        for i in range(len(num_s)):
                sum += math.factorial(int(num_s[i]))
        if sum == count:
                sum_t += sum
                print(count)
        count += 1


end = time.clock()
print(sum_t)
print("Processint time:", Decimal(end) - Decimal(start), "seconds")

