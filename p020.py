# Project Euler - Problem 20
# -----------------------------------------------------------------------------
# Find the sum of the digits in the number 100!

import math
import time
start = time.time()

i = math.factorial(100)
s = str(i)
total = 0
for n in range(len(s)):
    total += int(s[n])

stop = time.time()
print(total)
print('Time: {} seconds'.format(stop-start))
