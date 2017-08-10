# Project Euler - Problem 6
# The sum of the squares of the first ten natural numbers is,
#	1^2 + 2^2 +...+ 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# 	(1 + 2 +...+ 10)^2 = 3025
# Hence, the difference between the sum of the squares of the first ten
# natural numbers and the square of the sum is 3025 - 385 = 2640.
# Find the difference between the sum of the squares of the first one
# hundred natural numbers and the square of the sum.

import time
start = time.time()

top = 100
total = int((top * (top + 1)/2)**2)
for i in range(top):
	total -= (i+1)**2
end = time.time()
print(total)
print('Processing Time: {} seconds'.format(end-start))
