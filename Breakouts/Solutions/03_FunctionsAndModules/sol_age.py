#!/usr/bin/env python
"""
   NASA Goddard Space Flight Center
          Python User Group
        2014 Python Boot Camp 

        BREAKOUT SOLUTION
     Adapted from the Berkeley Python Boot Camp
"""

# Import the datetime module
#---------------------------
import datetime

print "==================================================="
print "------------------   Age Example  -----------------"
print "==================================================="

# Create a variable representing when John was born.
#---------------------------------------------------
born = datetime.datetime(1939, 10, 27)

# Create a variable representing now
#------------------------------------
now = datetime.datetime.now()

# Subtract the two, forming a new variable, which will be a
# datetime.timedelta() object.
john_age = now - born

# Print that variable.
#---------------------
print "John Age is: ", john_age

# Grab just the days
#-------------------
nDays = john_age.days
print "Number of days  John has been alive : ", nDays

# Get the number of hours
#------------------------
nHours = 24*nDays
print "Number of hours John has been alive : ", nHours

# What will be the date in 1000 days from now?
#---------------------------------------------
td = datetime.timedelta(days=1000)
print "In 1000 days it will be ", now + td  # this is a datetime object
print "==================================================="
