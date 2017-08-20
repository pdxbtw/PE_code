# Project Euler - Problem 27
# -----------------------------------------------------------------------------
# Euler discovered the remarkable quadradic formula:
# n^2 + n + 41
# It turns out that the formula will produce 40 primes for the consecutive
# values n = 0 to 39. However, when n = 40, 40^2 + 40 + 41 = 40(40+1) + 41 is
# divisible by 41, and certainly when n=41.

# The incredible formula n^2-79n+1601 was discovered, which produces 80 primes
# for the consecutive values n=0 to 79. The product of the coefficients, -79
# and 1601, is -126479.

# Consider quadratics of the form:
#     n^2+an+b, where |a|<1000 and |b|<1000
#     where |n| is the modulus/absolute value of n
#     e.g. |11| = 11 and |-4| = 4
# Find the product of the coefficients, a and b, for the quadratic expression
# that produces the maximum number of primes for consecutive values of n,
# starting with n=0.

import math
import time
start = time.time()

primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, )
test_val = 30
run = True
isprime = True
while test_val < int(1e4):
    test_val += 1
    stop = math.floor(math.sqrt(test_val))
    isprime = True
    for i in primes:
        if i > stop:
            break
        if test_val % i == 0:
            isprime = False
            break
    if isprime:
        primes += (test_val,)

streak_max = 1
a_max = 0
b_max = 0
for a in range(-1000, 1000):
    for b in primes:
        if b > 1000:
            break
        n = 1
        streak = 1
        while True:
            val = n**2 + a*n + b
            if val in primes:
                n += 1
                streak += 1
            else:
                if streak > streak_max:
                    streak_max = streak
                    a_max = a
                    b_max = b
                    print("streak = ", streak_max, " a = ", a, " b = ", b)
                break

stop = time.time()
print(streak_max)
print(a_max * b_max)
print("Time: {} seconds".format(stop-start))
