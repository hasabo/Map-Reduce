#!/usr/bin/env python3
"""mapper.py"""

import sys

# set the input that comes from STDIN to a varialble
infile = sys.stdin

# skip first line of first input file which is the header of the user table 
next(infile) 

for line in infile:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the row into cells 
    line = line.split('\t')
    # use NaN as output for the empty merged cells 
    UserId = "NaN"
    Name = "NaN"
    DOB = "NaN"
    UserIdFollower = "NaN"
    UserIdFollowing = "NaN"

    # identify the user table
    if len(line) ==3:
        # fill the non empty fileds 
        UserId = line[0]
        Name = line[1]
        DOB = line[2]
        # convert the key elements to a single string to be used a mapper key
        x = [UserId, Name, DOB, UserIdFollower, UserIdFollowing]
        y = ''
        for i in x:
            y = y + i + ','
        y = y.replace(' ,',',').rstrip(',')
        # tab-delimited output for merged cells whih have a mapper value 1
        print ( '%s\t%s' % (y,1) )
    else:
    # handle the second table so the output to have the same fields
    # fill the non empty cells
        UserIdFollower = line[0]
        UserIdFollowing = line[1]
# skip first line of second input file which is the header of the follow table 
        if UserIdFollower == 'UserIdFollower ':
            pass
        else:
        # convert the key elements to a single string to be used a mapper key
            x = [UserId, Name, DOB, UserIdFollower, UserIdFollowing]
            y = ''
            for i in x:
                y = y + i + ','
            y = y.replace(' ,',',').rstrip(',')
        # tab-delimited output for merged cells whih have a mapper value 1
            print ( '%s\t%s' % (y,1) )



