#!/home/wilson_b/anaconda3/bin/python
# !/home/fure_j/Software/pypy3-2.4-linux_x86_64-portable/bin/pypy

# -----------------------------------------------------------------------------
# If p is the perimeter of a right angle triangle with integral sides, {a,b,c},
# there are exactly three solutions for p = 120. {20,48,52}, {24,45,51},
# {30,40,50}
# For which value of p <= 1000, is the number of solutions maximised?

def even_odd_xor(a,b):
        a %= 2
        b %= 2
        return bool(a) != bool(b)

def iscoprime(a,b):
        if (a % 2 == 0) and (b % 2 == 0):
                # 2 is a common factor
                return False
        count = 3
        while count <= b:
                if (a % count == 0) and (b % count == 0):
                        return False
                count += 2
        return True

def condition(a,b):
        if even_odd_xor(a,b):
                if iscoprime(a,b):
                        return True
        return False

from decimal import *
import time
import pdb
getcontext().prec = 3
#pdb.set_trace()
start = time.clock()

trip = []
m = 1
temp = 0 
count = 0
run = True
while run:
        m += 1
        n = 1
        while n < m:
                if condition(m,n):
                        a = m**2 - n**2
                        b = 2*m*n
                        c = m**2 + n**2
                        d = a+b+c
                        if a > b:
                                temp = a
                                a = b
                                b = temp
                        if d < 1000:
                                trip.append([a,b,c,d])
                        count += 1
                        if count == 87:
                                run = False
                                break
                n += 1
trip.sort(key=lambda k: k[3])

trip_max = 0
trip_p = 0
#pdb.set_trace()
for i in range(12,1001):
        count = 0
        n = 0
        while n <= i//12:
                n += 1
                if i < n*12:
                        break

                j = 0
                while i >= n*12:
                        if j >= len(trip):
                                break
                        if i == n*trip[j][3]:
                                count += 1
                                if i == 120:
                                        print(trip[j])
                                if count > trip_max:
                                        trip_max = count
                                        trip_p = i
                        elif i < trip[j][3]:
                                break
                        j += 1
end = time.clock()
print(trip_max)
print(trip_p)
print("Processing time:", Decimal(end) - Decimal(start), "seconds")
