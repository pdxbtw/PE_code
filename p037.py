#!/home/fure_j/Software/pypy3-2.4-linux_x86_64-portable/bin/pypy
# !/home/wilson_b/anaconda3/bin/python

# Project Euler - Problem 37
# -----------------------------------------------------------------------------
# The number 3797 has an interesting property. Being prime itself, it is
# possible to continuously remove digits from left to right, and remain prime
# at each stage: 3797, 797, 97, and 7. Similarly, we can work from right to
# left: 3797, 379, 37, and 3.
# Find the sum of the only eleven primes that are both trucatable from left to
# right and right to left.
# NOTE: 2,3,5, and 7 are not considered to be trucatable primes.


import time
# import pdb
# pdb.set_trace()


def isprime(p_test=2, primes=[]):
    if len(primes) == 0:
        primes.append(2)
        primes.append(3)
        primes.append(5)
    if p_test in primes:
        return 1
    elif p_test < primes[-1]+1:
        return 0
    else:
        start = primes[-1]+2
        stop = p_test + 1
        for i in range(start, stop, 2):
            prime = True
            for j in primes:
                if j**2 > i:
                    break
                if i % j == 0:
                    prime = False
                    break
            if prime:
                primes.append(i)
        if primes[-1] == p_test:
            return 1
        else:
            return 0


def isprim_left(p_l_test, primes=[]):
    p_l_test //= 10
    while p_l_test:
        if p_l_test not in primes:
            return 0
        p_l_test //= 10
    return 1


def isprim_right(p_r_test, primes=[]):
    p_str = str(p_r_test)
    l_p = len(p_str)
    for i in range(l_p - 1):
        r_str = p_str[i+1:]
        if int(r_str) not in primes:
            return 0
    return 1


start = time.time()
primes = []
p_temp = []
p_left = []
right_left = []
num_prime = 4
temp_l = 0
order = 1
run = True
while run:
    order += 1
    top = int(10**order)
    isprime(top, primes)
    p_temp = primes[num_prime:]
    num_prime = len(primes)
    for i in p_temp:
        val_str = str(i)
        for j in val_str:
            if j in "0468":
                p_temp.remove(i)
                break
    for i in p_temp:
        if isprim_left(i, primes):
            p_left.append(i)
    for i in p_left:
        if isprim_right(i, primes):
            right_left.append(i)
            print(i)
            if len(right_left) == 11:
                run = False
                break
    del p_left[:]
    temp_l = len(p_temp)

stop = time.time()
print(sum(right_left))
print("Time: {} seconds".format(stop-start))
