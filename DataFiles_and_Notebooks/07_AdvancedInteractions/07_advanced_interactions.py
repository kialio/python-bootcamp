
# coding: utf-8

# <CENTER>
# <H1>
# NASA Goddard Space Flight Center <BR>
#     Python User Group <BR>
# 2014 Python Boot Camp
# </H1>
# </CENTER>

# # Advanced Interactions
# 
# Today you're no longer python novices. Now let's try some advanced interactions.
# 
#     •	lambda functions
# 	•	filter, map, reduce, zip
# 	•	try, except, finally
# 	•	exec, eval
# 
# 

# ## Lambda Functions
# 
# (anonymous functions)
# from Lisp & functional programming.
# 
# Allow functions to be defined without an (explicit) identifier.

# In[1]:

tmp = lambda x: x**2
print  type(tmp)


# In[2]:

tmp(2)


# In[3]:

# forget about creating a new function name...just do it!
(lambda x,y: x**2+y)(2,4.5)


# In[4]:

## create a list of lambda functions
lamfun = [lambda x: x**2, lambda x: x**3,            lambda y: math.sqrt(y) if y >= 0 else "Really? I mean really? %f" % y]


# In[5]:

for l in lamfun: print l(-1.3)


# lambda functions are meant to be short, one liners. If you need more complex functions, probably better just to name them

# ### An example: sorting lists
# Recall our list of meetings from Monday's Breakout 2 (Advanced Data Structures). Let's understand that one-line solution.

# In[14]:

# includes the meeting, room, day, start time(decimal hours), end time
meetings = [("Gamma-Ray Burst Lunch","B34 E256","Tue",12.0,13.0),            ("Extragalactic Journal Club","B34 S391","Tue",14.0,15.0),             ("Python Users Group","B34 W120A/B","Tue",14.5,15.5),             ("Astrophysics Colloquium","B34 E215","Tue",15.5,17.0),             ("NGAPS Happy Hour","B34 E215","Tue",17.0,18.0),             ("Exoplanet Club","B34 E215","Tue",11.5,12.5),             ("IS&T Colloquium Series","B3 Auditorium","Tue",11.0,12.0) ]

# we'll also define a helpful function to print our sorted schedules
def print_schedule (meetings):
    print "%.32s %.14s %.4s %.5s" % ("Meeting"+32*' ', "Room No."+14*' ', "Day"+4*' ', "Time"+5*' ')
    print "-"*60
    for meeting in meetings:
        print "%.32s %.14s %.4s %.5s" % (meeting[0]+32*' ', meeting[1]+14*' ', meeting[2]+4*' ', str(meeting[3])+5*' ')


# In[18]:

#sort meetings by start time:
meetings.sort(key = lambda x: x[3])
print_schedule(meetings)


# Since the breakout, I've thought of some other meetings I should add to my schedule... but now we need to also sort by the Day of the week, then time.

# In[23]:

my_schedule=meetings+[("Fermi Journal Club","B34 E256","Wed",15.5,16.5),          ("SEAL Talk","B34 E215","Thu",12.0,13.5),           ("SED Director's Seminar","B33 H114","Fri",12.0,13.0),           ("Engineering Colloquium","B3 Auditorium","Mon",15.5,16.5),           ("Goddard Scientific Colloquium","B3 Auditorium","Fri",15.5,16.5),           ("IS&T Colloquium Series","B3 Auditorium","Tue",11.0,12.0)]
print_schedule(my_schedule)


# <BR>
# An easy way to sort lists using multiple columns is 
# ***operator.itemgetter***

# In[24]:

import operator
help(operator.itemgetter)


# In[25]:

# Sort first by day, then by time
my_schedule.sort(key=operator.itemgetter(2,3))
print_schedule(my_schedule)


# <BR>*Wait!* That's not what we wanted. Days of the week aren't ordered alphabetically, but we can make that order explicit using a tuple and sort using another lambda function.

# In[28]:

days_of_week=('Mon','Tue','Wed','Thu','Fri')
my_schedule.sort(key = lambda x: (days_of_week.index(x[2]),x[3]) )
print_schedule(my_schedule)


# ##filter, map, reduce, zip
# 
# **filter** is a certain way to do list comprehension
# 
# `filter(function, sequence)` returns a sequence consisting of those items from the sequence for which function(item) is true.
# 

# In[29]:

#Create a list for which numbers between 0 and 100 are even and divisible by 11

#old way: list comprehension
mylist=[num for num in xrange(101) if (num % 2 == 0.0) and (num % 11 == 0.0)]
print mylist


# In[30]:

#new way: filter
def f(num): return (num % 2 == 0.0) and (num % 11 == 0.0)
mylist = filter(f,xrange(101))
print mylist


# if the input is a string, so is the output...

# In[34]:

## also works on strings...try it with lambdas!
a="Charlie Brown said \"!@!@$@!\""; print a


# In[35]:

# Get just the alphabetical characters:
import string
filter(lambda c: c in string.ascii_letters,a)


# In[ ]:

`filter` is also useful 

xrange() is an iterable version of range():
range(10) creates a 10-element list,
xrange(10) creates an iterable object which returns 0 the first time it’s called, 1 the next time, etc. 

Is there a computational advantage? 
Time how long it takes with the ipython magic %timeit:

### need to edit ###




# In[38]:

def f(num): return (num % 2 == 0.0) and (num % 11 == 0.0)
get_ipython().magic(u'timeit len(filter(f,range(1L)))')
get_ipython().magic(u'timeit len(filter(f,xrange(1L)))')


# ### `map` is just another way to do list comprehension ###
# 
# `map(function, sequence)` calls `function(item)` for each of the sequence's items and returns a list of the return values

# In[40]:

def cube_it(x): return x**3

map(cube_it,xrange(1,10))


# In[42]:

map(lambda x: x**3, xrange(1,10))


# ### `reduce` returns one value ###
# 
# reduce(function, sequence) returns a single value constructed by calling the binary function function on the first two items of the sequence, then on the result and the next item, and so on

# In[47]:

# sum from 1 to 10
reduce(lambda x,y: x + y, xrange(1,11))   
get_ipython().magic(u'timeit reduce(lambda x,y: x + y, xrange(1,11))')


# In[48]:

# sum() is a built in function...it’s bound to be faster
get_ipython().magic(u'timeit sum(xrange(1,11))')


# ###  `zip()` ###
# 
# built in function to pairwise concatenate items in iterables into a list of tuples

# In[53]:

print zip(["I","you","them"],["=spam","=eggs","=dark knights"])
print zip(["I","you","them"],["=spam","=eggs","=dark knights"],["!","?","#"])
print zip(["I","you","them"],["=spam","=eggs","=dark knights"],["!","?"])


# In[54]:

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
  print 'What is your %s?  It is %s.' % (q, a)


# not to be confused with `zipfile` module which exposes file compression 

# ## `try`, `except`, `finally`
# 
# Not all of our code is well-written. Here's how we can manage.

# In[87]:

# what happens when you don't give a number?
tmp = raw_input("Enter a number and I'll square it: ")
print float(tmp)**2


# Solution: Wrap volatile code in try/except/finally
# ![diagram of try, except, finally](https://raw.githubusercontent.com/kialio/python-bootcamp/master/Lectures/07_Introduction/tryexceptfinally.png)
# 

# In[56]:

#this code can gracefully handle non-numbers
try:   
    tmp = raw_input("Enter a number “ + and I'll square it: ")
    print float(tmp)**2
except:
    print "dude. I asked you for a number and " + "%s is not a number." % tmp
finally:
    print "thanks for playing!"


# #### A quick work on exception handling in python
# 
#  * errors in Python generate what are called “exceptions”
#  * exceptions can be handled differently depending on what kind of exception they are. (we’ll see more of that later)
#  * except “catches” these exceptions
#  * you do not have to catch exceptions (try/finally) is allowed. Finally block is executed no matter what! 

# ## `exec`, `eval`
# 
# `exec` executes strings as if they were Python code.

# In[106]:

a = "print 'checkit' "
exec a


# In[107]:

a = "x = 4.56"
exec a
print x


# In[108]:

exec "del x"
print x


# This has some clear benefits:
#   * dynamically create Python code
#   * execute that code w/ implication for current namespace 

# In[116]:

# try the following answers:
#what built in function would you like me to coopt? math.sin
#what new name would you like to give it? monty_sin
#what built in function would you like me to coopt? Range
#what new name would you like to give it? python_range

import math
nn = True
while nn != 'stop':
    bi = raw_input("what built in function would you like me to coopt? ")
    nn = raw_input("what new name would you like to give it? ")
    exec "%s = %s" % (nn,bi)


# In[86]:

# If you tried turning math.sin into monty_sin 
# and range into python_range this will work!
print monty_sin (math.pi/2)
print python_range(3)


# `eval` evaluates strings as Python expressions 

# In[111]:

x = eval('5') ; print x
x = eval('abs(%d)' % -100) ; print x


# In[112]:

x = eval('print 5')


# In[113]:

exec "print 5"


# In[114]:

x = eval('if 1: x = 4')


# In[115]:

exec "if True: x=4" ; x


# <br><p>
# Now you have all the tools you need to write code that practically writes itself...

# ##Breakout 7
# 
# Survival Driven Development
# ===========================
# 
# Survival Driven Development (SDD) is the newest software development fad.  In this development framework, you specify what the software is supposed to do, then randomly generate source code to fulfill these requirements.  Most of these attempts will fail, but hopefully one will succeed.
# 
# Your task is to use SDD to make a function to approximate `x**2 + x`.
# 
# Hint 1: Randomly generate lambda functions using a restricted vocabulary of source fragments.<br>
# `vocab = ['x', 'x', ' ', '+', '-', '*', '/', '1', '2', '3']`
# 
# Hint 2: Only evaluate `x` at a small-ish number of values and save the difference between those answers and the true value of `x**2 + x`.
# 
# Hint 3: SDD is error prone.  Be sure to catch your errors!

# ![How could you possibly think typing "import skynet" was a good idea?](http://imgs.xkcd.com/comics/2008_christmas_special.png)

# In[105]:

# if you were having trouble getting started...
import random
import numpy

vocab = ["x","x","","+","-","*","/","1","2","3"]

max_try = 1000000
max_chars = 10  #max number of characters to generate
x_array = numpy.arange(-3,3,0.4) # over a smallish range
real_function = x_array**2 + x_array

tries = []

# for loop...
# you fill in the rest

