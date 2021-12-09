#############################################################################
##
## CS 101 Lab
## Lab 13
## Lily Dang
## ldkvd@mail.umkc.edu
##
## PROBLEM:
##
## ALGORITHM:
##  1. Start.
##  2. Import math.
##  3. Define a function that takes a parameter that is a list and returns
##     the total sum of all the values in the list passed.
##  4. Define a function that takes a parameter that is a list and returns
##     the average of all the values in the list passed.
##  5. Define a function that takes a parameter that is a list and returns
##     the median value of a list.
##  6. Stop.
##
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
##############################################################################


import math

def total(values:list):
    return sum(values)

def average(values:list):
    if values == []:
        return math.nan
    else:
        sum_values = sum(values)
        avg = sum_values/len(values)
        return float(avg)

def median(values:list):
    values = sorted(values)
    length = len(values)
    if values == []:
        raise ValueError
    elif length % 2 == 0:
        mid1 = int((length/2) - 1)
        mid2 = int(length/2)
        median = float(values[mid1] + values[mid2])/2
        return median
    else:
        median = values[int((length-1)/2)]
        return median
