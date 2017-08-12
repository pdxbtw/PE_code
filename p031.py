#!/home/fure_j/Software/pypy3-2.4-linux_x86_64-portable/bin/pypy 
# !/home/wilson_b/anaconda3/bin/python

# Project Euler - Problem 31
# -----------------------------------------------------------------------------
# In England the currency is made up of pound and pence and there are eight 
# coins in general circulation: 1p, 2p, 5p, 10, 20, 50, L1(100p) and L2(200p).
# It is possible to make L2 in the following way:
#       1xL1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
# How many different ways can L2 be made using any number of coins?

from decimal import *
import time
import pdb
import math
getcontext().prec = 3
#pdb.set_trace()
start = time.clock()

num_ways = 0
tot = 0
l2  = 0
l1  = 0
p50 = 0
p20 = 0
p10 = 0
p5  = 0
p2  = 0
p1  = 0
while 1:
        if tot >= 200:
                if tot == 200:
                        num_ways += 1
                l2 = 0
                tot = 0
                break
        while 1:
                if tot >= 200:
                        if tot == 200:
                                num_ways += 1
                        l1 = 0
                        tot = 0
                        break
                while 1:
                        if tot >= 200:
                                if tot == 200:
                                        num_ways += 1
                                p50 = 0
                                tot = 0
                                break
                        while 1:
                                if tot >= 200:
                                        if tot == 200:
                                                num_ways += 1
                                        p20 = 0
                                        tot = 0
                                        break
                                while 1:
                                        if tot >= 200:
                                                if tot == 200:
                                                        num_ways += 1
                                                p10 = 0
                                                tot = 0
                                                break
                                        while 1:
                                                if tot >= 200:
                                                        if tot == 200:
                                                                num_ways += 1
                                                        p5 = 0
                                                        tot = 0
                                                        break
                                                while 1:
                                                        if tot >= 200:
                                                                if tot == 200:
                                                                        num_ways += 1
                                                                p2 = 0
                                                                tot = 0
                                                                break
                                                        while 1:
                                                                if tot >= 200:
                                                                        if tot == 200:
                                                                                num_ways += 1
                                                                        p1 = 0
                                                                        tot = 0
                                                                        break
                                                                p1 += 1
                                                                tot = (l2*200 + l1*100 + p50*50 + p20*20 + p10*10 + p5*5 + p2*2 + p1*1)
                                                        p2 += 1
                                                        tot = (l2*200 + l1*100 + p50*50 + p20*20 + p10*10 + p5*5 + p2*2 + p1*1)
                                                p5 += 1
                                                tot = (l2*200 + l1*100 + p50*50 + p20*20 + p10*10 + p5*5 + p2*2 + p1*1)
                                        p10 += 1
                                        tot = (l2*200 + l1*100 + p50*50 + p20*20 + p10*10 + p5*5 + p2*2 + p1*1)
                                p20 += 1
                                tot = (l2*200 + l1*100 + p50*50 + p20*20 + p10*10 + p5*5 + p2*2 + p1*1)
                        p50 += 1
                        tot = (l2*200 + l1*100 + p50*50 + p20*20 + p10*10 + p5*5 + p2*2 + p1*1)
                l1 += 1 
                tot = (l2*200 + l1*100 + p50*50 + p20*20 + p10*10 + p5*5 + p2*2 + p1*1)
        l2 += 1
        tot = (l2*200 + l1*100 + p50*50 + p20*20 + p10*10 + p5*5 + p2*2 + p1*1)
end = time.clock()
print(num_ways)
print("Processint time:", Decimal(end) - Decimal(start), "seconds")

