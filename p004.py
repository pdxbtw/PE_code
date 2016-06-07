# Project Euler - Problem 4
# A palindromic number reads the same both ways. The largest palindrome
# made from the product of two digit numbers is 9009 = 91 * 99.
# Find the largest palindrome made from the product of two 3-digit numbers

from decimal import *
import time
getcontext().prec = 3
start = time.clock()

max_val = 0
for i in range(999, 900, -1):
	for j in range(i, 900, -1):
		a = i * j
		s = str(a)
		if s[0] == s[-1] and s[1] == s[-2] and s[2] == s[-3]:
			if a > max_val:
				max_val = a

end = time.clock()
print(max_val)
print('Processing Time:', Decimal(end) - Decimal(start), 'seconds')

