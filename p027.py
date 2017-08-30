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


def primeSieve(bound):
    aprox_primes = math.floor(bound / (math.log(bound) - 1.0836))
    primes = [0] * aprox_primes
    primes[0] = 2
    n = 3
    count = 1
    while count < aprox_primes:
        prime = True
        max_search = math.sqrt(n)
        for i in primes:
            if i > max_search:
                break
            if not n % i:
                prime = False
                break
        if prime:
            primes[count] = n
            count += 1
        n += 2
    return primes


def findPrimeCoef(primes, bound):
    streak_max = 1
    a_max = 0
    b_max = 0
    for a in range(-bound, bound):
        for b in primes:
            if b > bound:
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
                    break
    return streak_max, a_max, b_max


start = time.time()
primes = primeSieve(4000)
streak_max, a, b = findPrimeCoef(primes, 1000)
stop = time.time()
print(streak_max)
print(a * b)
print("Time: {} seconds".format(stop-start))
