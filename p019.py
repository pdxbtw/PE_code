# Project Euler - Problem 19
# -----------------------------------------------------------------------------
# You are given the following information, but you may prefer to do some
# research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
#    April, June and November.
#    All the rest have thirty-one,
#    Saving February alone,
#    Which has twenty-eight, rain or shine.
#    And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century
#    unless it is divisible by 400.

# How many Sundays fell on the first of the month during the twentieth
# century (1 Jan 1901 to 31 Dec 2000)?

import time


def numSundays(start_year, end_year):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June',
              'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    mon_dict = {'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30,
                'May': 31, 'June': 30, 'July': 31, 'Aug': 31,
                'Sep': 30, 'Oct': 31, 'Nov': 30, 'Dec': 31}

    day_of_week = 1    # Our start date is a Monday. Sun=0, Mon=1, Tue=2, etc.
    for month in months:    # Go through 1900 to find 1901 start day
        day_of_week += mon_dict[month]

    day_of_week %= 7
    n_sundays = 0
    for y in range(start_year, end_year+1):
        for month in months:
            if day_of_week == 0:
                # print('{} 1, {}'.format(month, y))
                n_sundays += 1

            day_of_week += mon_dict[month]
            if month == 'Feb' and y % 4 == 0:
                day_of_week += 1
            day_of_week %= 7
    return n_sundays


start = time.time()
ans = numSundays(1901, 2000)
stop = time.time()
print(ans)
print("Time: {} seconds".format(stop-start))
