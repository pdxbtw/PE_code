#!/home/fure_j/Software/pypy3-2.4-linux_x86_64-portable/bin/pypy
# !/home/wilson_b/anaconda3/bin/python

# Project Euler - Problem 30
# -----------------------------------------------------------------------------
# Surprisingly, there are only three numbers that can be written as the sum of
# fourth powers of their digits: 1634, 8208, 9474
# As 1 is not a sum, it is not included.
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
# Find the sum of all the numbers that can be written as the sum of 5th powers
# of their digits.

from decimal import *
import time
import pdb
getcontext().prec = 3
#pdb.set_trace()
start = time.clock()

count = 10
sum_t = 0
while count < 2e5:
        num_s = str(count)
        sum = 0
        for i in range(len(num_s)):
                sum += int(num_s[i]) ** 5
        if sum == count:
                sum_t += sum
        count += 1

end = time.clock()
print(sum_t)
print("Processing time:", Decimal(end) - Decimal(start), "seconds")
