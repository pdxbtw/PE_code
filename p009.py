# Project Euler - Problem 9
# A Pythagorean triplet is a set of three natural numbers, a<b<c, for which
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000
# Find the product of a*b*c.

import time
import decimal
getcontext().prec = 3
start = time.clock()

max_val = 1000
a = 1
b = 2
c = max_val - a - b
while a < c+1:
	while b < c:
		if (a**2 + b**2) == c**2:
			print(a*b*c)
			break
		c -= 1
		b += 1
	a += 1
	b = a + 1
	c = max_val - a - b
end = time.clock()
print('Processing Time:', Decimal(end) - Decimal(start), 'seconds')
print(count)

