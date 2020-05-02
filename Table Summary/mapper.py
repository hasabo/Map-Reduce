#!/usr/bin/env python3
"""mapper.py"""

import sys

# set the input that comes from STDIN to a varialble
infile = sys.stdin

# skip first line of input file which is the header of input table
next(infile) 

for line in infile:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the row into cells with maxsplit 2 since there are 3 columns
    line = line.split('\t', 2)
    # tab-delimited output for student ID and grade.
    # Every output line considered as 1 module.
    print ( '%s\t%s' % (line[0],line[2]) )
    



