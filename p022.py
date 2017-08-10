# Project Euler - Problem 22
# -----------------------------------------------------------------------------
# Using names.txt, a 46K text file containing over five thousand first names, 
# begin by sorting it into alphabetical order. Then working out the alphabetical
# value for each name, multiply this value by its alphabetical position in the 
# list to obtain a name score.
# For example, when the list is sorted into alphabetical order, COLIN, which is
# worth 3+15+12+9+14=53, is the 938th name in the list. So, COLIN would obtain
# a score of 938x53=49714.
#
# What is the total of all the name scores in the file?

import time
start = time.time()

f = open('p022_names.txt', 'r')
s = f.read();
f.close()
s = s.replace(",", "\n")
s += "\n"
s = s.replace('"', "")
g = open('temp.txt', 'w')
g.write(s)
g.close()


g = open('temp.txt', 'r')
names = ["$"]*6000
n = 0
for line in g:
        names[n] = line
        n += 1
g.close()
names = [x for x in names if x != "$"]
names.sort()

prodsum = 0
for i in range(n):
        temp_sum = 0
        temp = names[i]
        for j in range(len(temp)-1):
                temp_sum += (ord(temp[j]) - 64)
        prodsum += (temp_sum * (i+1))

end = time.time()
print(prodsum)
print('Processing Time: {} seconds'.format(end-start))
