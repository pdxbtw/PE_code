# Project Euler - Problem 17
# -----------------------------------------------------------------------------
# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out
# in words, how many letters would be used?

# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
# forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
# letters. The use of "and" when writing out numbers is in compliance with
# British usage.

import time


def num2word(num):
    word = "x"  # Create non empty string
    ones = num % 10
    tens = (num % 100) // 10
    hund = (num % 1000) // 100
    thou = num // 1000

    # Add thousands if any
    if thou:
        word = "".join([word, onesdig(thou), "thousand"])
    # Add hundreds if any
    if hund:
        word = "".join([word, onesdig(hund), "hundred"])
    # Add "and" if greater than 100 and has any tens or ones digits
    if (thou or hund) and (tens or ones):
        word = "".join([word, "and"])
    # Handle teens, twenties, thirties, etc.
    if tens:
        if tens == 1:
            word = "".join([word, teens(ones)])
        elif tens and ones:
            word = "".join([word, doubledig(tens), onesdig(ones)])
        else:
            word = "".join([word, doubledig(tens)])
    elif ones:
        word = "".join([word, onesdig(ones)])
    return word[1:]  # Remove leading "x" character


def onesdig(num):
    if num == 1:
        return "one"
    elif num == 2:
        return "two"
    elif num == 3:
        return "three"
    elif num == 4:
        return "four"
    elif num == 5:
        return "five"
    elif num == 6:
        return "six"
    elif num == 7:
        return "seven"
    elif num == 8:
        return "eight"
    else:
        return "nine"


def teens(num):
    if num == 0:
        return "ten"
    elif num == 1:
        return "eleven"
    elif num == 2:
        return "twelve"
    elif num == 3:
        return "thirteen"
    elif num == 4:
        return "fourteen"
    elif num == 5:
        return "fifteen"
    elif num == 6:
        return "sixteen"
    elif num == 7:
        return "seventeen"
    elif num == 8:
        return "eighteen"
    else:
        return "nineteen"


def doubledig(num):
    if num == 2:
        return "twenty"
    elif num == 3:
        return "thirty"
    elif num == 4:
        return "forty"
    elif num == 5:
        return "fifty"
    elif num == 6:
        return "sixty"
    elif num == 7:
        return "seventy"
    elif num == 8:
        return "eighty"
    else:  # num == 9:
        return "ninety"


start = time.time()
letter_count = 0
bound = 1000
for i in range(bound):
    letter_count += len(num2word(i+1))
stop = time.time()
print('There are {} letters from 1 to {}'.format(letter_count, bound))
print('Time: {} seconds'.format(stop-start))
