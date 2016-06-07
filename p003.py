# Project Euler - Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import time
import decimal
getcontext().prec = 3
start = time.clock()

num = 600851475143
max_prime = 3

count = 3
while count <= num:
        if not num % count:
                max_prime = count
                num = num / count
        else:
                count += 2
end = time.clock()
print(max_prime)
print('Processing Time:', Decimal(end) - Decimal(start), 'seconds')

