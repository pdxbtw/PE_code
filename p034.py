# Project Euler - Problem 34
# -----------------------------------------------------------------------------
# 145 is a curious number, as 1! + 4! + 5! = 145. Find the sum of all numbers
# which are equal to the sum of the factorial of their digits.
# Note: as 1! and 2! are not sums, they are not included.

import time
import math
# import pdb
# pdb.set_trace()
start = time.time()

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


stop = time.time()
print(sum_t)
print("Time: {} seconds".format(stop-start))
