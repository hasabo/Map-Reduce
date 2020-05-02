#!/usr/bin/env python3
"""reducer.py"""

from operator import itemgetter
import sys

# set variables 
even_count = 0
odd_count = 0
word = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if word == 'even:':
        even_count += count
    else:
        odd_count += count
# output the total counted even and odd word
print ('even:\t%s,\todd:\t%s' % (even_count, odd_count))
