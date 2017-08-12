#!/home/wilson_b/anaconda3/bin/python
# !/home/fure_j/Software/pypy3-2.4-linux_x86_64-portable/bin/pypy 

# Project Euler - Problem 48
# -----------------------------------------------------------------------------
# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

from decimal import *
import math
import time
import pdb
#pdb.set_trace()
getcontext().prec = 3
start = time.clock()

sum = 0
for i in range(1,1001):
        sum += i ** i
ans = str(sum)

end = time.clock()
print(ans[-10:])
print("Processing Time:", Decimal(end) - Decimal(start), "seconds")
