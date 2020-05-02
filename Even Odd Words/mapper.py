#!/usr/bin/env python3
"""mapper.py"""

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    # increase counters
    for word in words:
        # write the results to STDOUT (standard output);
        # tab-delimited output the even and odd words
        if len(word) % 2 == 0:
            print('even:\t%s' %1)
        else:
            print('odd:\t%s' %1)




