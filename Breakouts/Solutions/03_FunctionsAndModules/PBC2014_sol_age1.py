#!/usr/bin/env python
"""
   NASA Goddard Space Flight Center
          Python User Group
        2014 Python Boot Camp  

        BREAKOUT SOLUTION
     Adapted from the Berkeley Python Boot Camp
"""

# Import the modules
#-------------------
import datetime
import sys

def days_from_now(ndays):
    """
      Input:
         - ndays: number of days
      Returned value:
         - date ndays from now
    """
    now = datetime.datetime.now()
    new = now + datetime.timedelta(int(ndays)) 
    return "In " + str(ndays) + " days the date will be: " + str(new)

def days_since(year, month, day): 
    """
      Using a date (year, month and day) in the past,
      returns the number of days since then.

      Input:
         - year:
         - month: 
         - day: 
      Returned value:
         - String reporting the number of days since some time
    """
    now = datetime.datetime.now()
    then = datetime.datetime(year, month, day)
    diff = now - then
    a = str(year)+"/"+str(month)+"/"+str(day)
    return "Number of days since %s: %s " %(a, str(diff.days))

if __name__ == "__main__":
    """
      Executed only if run from the command line.
      Call with

          age1.py <year> <month> <day>

      to list the days since that date, or

          age1.py  <day>

      to list the date in some number of days
    """
    print "==================================================="
    print "------------------  Age1 Example  -----------------"
    print "==================================================="

    if len(sys.argv) == 2 :
       result = days_from_now(int(sys.argv[1]))
    elif len(sys.argv) == 4 :
       year = int(sys.argv[1])
       month = int(sys.argv[2])
       day = int(sys.argv[3])
       result = days_since(year, month, day)
    else : 
       result = "Error : don't know what to do with "+repr(sys.argv[1:])

    print result
    print "==================================================="
