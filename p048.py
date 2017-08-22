# Project Euler - Problem 48
# -----------------------------------------------------------------------------
# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

import time
start = time.time()

sum = 0
for i in range(1, 1001):
        sum += i ** i
ans = str(sum)

stop = time.time()
print(ans[-10:])
print("Time: {} seconds".format(stop-start))
