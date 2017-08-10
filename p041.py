# Project Euler - Problem 41
# -----------------------------------------------------------------------------
# We shall say that an n-digit number is pandigital if it makes use of all the
# digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
# also prime.
# What is the largest n-digit pandigital prime that exists?

def permute(xs, low=0):
        if low + 1 >= len(xs):
                yield xs
        else:
                for p in permute(xs, low + 1):
                        yield p
                for i in range(low + 1, len(xs)):
                        xs[low], xs[i] = xs[i], xs[low]
                        for p in permute(xs, low + 1):
                                yield p
                        xs[low], xs[i] = xs[i], xs[low]
def isprime(num):
        if num % 2 == 0:
                return 0
        test = 3
        while test**2 <= num:
                if num % test == 0:
                        return 0
                test += 2
        return 1

import time
start = time.time()

max_prime = 0
for p in permute([7,6,5,4,3,2,1]):
        temp = 0
        for i in range(7):
                temp += p[i] * 10**(6-i)
        if isprime(temp):
                if temp > max_prime:
                        max_prime = temp

end = time.time()
print(max_prime)
print('Processing Time: {} seconds'.format(end-start))
