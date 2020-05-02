#!/usr/bin/env python3
"""reducer.py"""

import sys
# set  variables
follow_dict ={} # dictionary for the follow table
user_dict={} # dictionary for the user table
current_UserIdFollowing = None
count = [] # accumlate the followers

# Tab-delimited output header for the output table
print ('%s\t%s\t%s' % ('UserId', 'NameFollower', 'NameFollowing'))

# input comes from mapper output as STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the input we got from mapper.py
    y,c = line.split('\t')
    # splitting the mapper key output into variables to get the hidden data
    y = y.strip(',').split(',')
    UserId, Name, DOB, UserIdFollower, UserIdFollowing = y
    # process the merged data from the follow table
    if UserId == "NaN":
        # stack the followers for following userid
        if current_UserIdFollowing == UserIdFollowing:
            count.append(UserIdFollower)
            follow_dict[UserIdFollowing] = count
        else:
            current_UserIdFollowing = UserIdFollowing
            count = []
            count.append(UserIdFollower)
            follow_dict[UserIdFollowing]=count
    else:
        # process the merged data from user table
        user_dict[UserId] = [Name, DOB]
# serach for the matched users and prepare the output table
for i in user_dict.keys():
    if user_dict[i][1] <= '2002-03-01':
        NameFollowing = user_dict[i][0]
        for j in range ( len (follow_dict[i])):
            NameFollower = user_dict[follow_dict[i][j]][0]
            for  k,v in user_dict.items():
                if v[0] == NameFollower:
                    UserId = k
            # write result to STDOUT
            print ('%s\t%s\t%s' % (UserId, NameFollower, NameFollowing))

