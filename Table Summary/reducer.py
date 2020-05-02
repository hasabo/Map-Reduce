#!/usr/bin/env python3
"""reducer.py"""

from operator import itemgetter
import sys

# set local variables
current_student = None
previous_grade = 0 
current_grade = 0
min_grade = 0
max_grade = 0 
student = None
module_count = 0 

# Tab-delimited output header for the output table
print ('%s\t%s\t%s\t%s' % ('StudentId','MinGrade','MaxGrade', 'Modules'))

# input comes from  mapper output as STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    student, grade = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        grade = int(grade)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_student == student:
        module_count += 1
        # grade comparision to current grade to get the min and max grade
        if grade < current_grade:
            min_grade = grade
        elif grade > current_grade:
            max_grade = grade
    else:
        if current_student:
            # write result to STDOUT
            print ('%s\t%s\t%s\t%s' % (current_student,min_grade,max_grade, module_count))
        #update the variables
        current_grade = grade
        min_grade = grade
        max_grade = grade
        current_student = student
        module_count = 1
            
# output the last student record 
print ('%s\t%s\t%s\t%s' % (current_student,min_grade,max_grade, module_count))


