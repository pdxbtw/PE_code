#!/home/wilson_b/anaconda3/bin/python

# Project Euler - Problem 28
# -----------------------------------------------------------------------------
# Starting with the number 1 and moving to the right in a clockwise direction
# a 5 by 5 spiral is formed as follows:
#
#           21  22  23  24  25
#           20   7   8   9  10
#           19   6   1   2  11
#           18   5   4   3  12
#           17  16  15  14  13
#
# It can be verified that the sum of the numbers on the diagonal is 101.
# What is the sum of the numbers on the diagonal in a 1001 by 1001 spiral?

from decimal import *
import time
getcontext().prec = 3
start = time.clock()

order = 1001
sum = 0
for i in range(3, order + 1, 2):
        sum += i**2

for i in range(2, order + 1, 2):
        sum += 1 + i**2

prev = 1
for i in range(order):
        next = 2*i + prev
        sum += next
        prev = next


end = time.clock()
print(sum)
print("Processing time:", Decimal(end) - Decimal(start), "seconds")
