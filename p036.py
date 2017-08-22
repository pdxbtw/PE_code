#!/home/fure_j/Software/pypy3-2.4-linux_x86_64-portable/bin/pypy
# !/home/wilson_b/anaconda3/bin/python

# Project Euler - Problem 36
# -----------------------------------------------------------------------------
# The decimal number, 585 = 1001001001(binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in
# base 10 and base 2.
# (Please note that the palindromic number, in either base, may not include
# leading zeros.)

import time
# import pdb
start = time.time()

pal = True
total = 0
for i in range(int(1e6)):
    pal = True
    num_s = str(i)
    for j in range(len(num_s)//2):
        if num_s[j] != num_s[-(j+1)]:
            pal = False
            break
    if pal:
        temp = bin(i)
        num_b = temp[2:]
        for k in range(len(num_b)//2):
            if num_b[k] != num_b[-(k+1)]:
                pal = False
                break
            else:
                pal = True
        if pal:
            total += i

stop = time.time()
print(total)
print("Time: {} seconds".format(stop-start))
