# Project Euler - Problem 20
# -----------------------------------------------------------------------------
# Find the sum of the digits in the number 100!

import math
i = math.factorial(100)
s = str(i)
total = 0
for n in range(len(s)):
    total += int(s[n])
print(total)

