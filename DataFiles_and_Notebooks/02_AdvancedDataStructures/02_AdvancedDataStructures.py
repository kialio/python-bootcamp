
# coding: utf-8

# ## There are four main types of collections of data ("Sequence objects") ##
# 
# 	•	Lists: a mutable array of data
# 	•	Tuples: ordered, immutable list
# 	•	Sets: unordered collection of unique elements
# 	•	Dictionaries: keyword/value lookup
# 
# The value in each element can be whatever (type) you want.
# > string is actually a sequence object

# ### List ###
# #### denoted with a brackets ####

# In[6]:

v = [1,2,3] ; print len(v), type(v)


# In[7]:

v[0:2]


# In[8]:

v = ["eggs","spam",-1,("monty","python"),[-1.2,-3.5]]
len(v)


# In[9]:

v[0] ="green egg"
v[1] += ",love it."
v[-1]


# In[10]:

v[-1][1] = None ; print v


# In[11]:

v = v[2:] ; print v


# In[12]:

# let's make a proto-array out of nested lists
vv = [ [1,2], [3,4] ]


# In[13]:

print len(vv)


# In[14]:

determinant = vv[0][0]*vv[1][1] - vv[0][1]*vv[1][0]
print determinant


# the main point here: lists are **changeable** ("mutable")

# ### lists can be extended & appended ###

# In[15]:

v = [1,2,3]
v.append(4)   
v.append([-5]) ; print v


# > Lists can be considered objects.
# **Objects** are like animals: they know how to do stuff (like eat and sleep), they know how to interact with others (like make children), and they have characteristics (like height, weight).
# 
# > "Knowing how to do stuff" with itself is called a method. In this case "append" is a method which, when invoked, is an action that changes the characteristics (the data vector of the list itself).

# In[11]:

v = v[:4]
w = ['elderberries', 'eggs']
v + w


# In[12]:

v.extend(w) ; print v


# In[13]:

v.pop()


# In[14]:

print v


# In[15]:

v.pop(0) ; print v ## pop the first element


#  * `.append()`: adds a new element
#  * `.extend()`: concatenates a list/element
#  * `.pop()`: remove an element

# #### lists can be searched, sorted, & counted ####

# In[16]:

v = [1,3, 2, 3, 4, 'elderberries']
v.sort() ; print v


# `reverse` is a keyword of the `.sort()` method

# In[17]:

v.sort(reverse=True) ; print v


# `.sort()` changes the the list in place 

# In[18]:

v.index(4)   ## lookup the index of the entry 4


# In[19]:

v.index(3)


# In[20]:

v.count(3)


# In[21]:

v.insert(0,"it's full of stars") ; print v


# In[22]:

v.remove(1) ; print v


#  &nbsp;

# ### IPython is your new best friend ##
# 
# 1. Type `v.` then the Tab button
# 
# 2. Type `v.re` then the Tab button
# 
# 3. Type `v.remove?`

# In[23]:

## try it here


#  &nbsp;

# ### List ###
# #### iteration ####

# In[24]:

a = ['cat', 'window', 'defenestrate']
for x in a:
       print x, len(x)


# In[25]:

for i,x in enumerate(a):
       print i, x, len(x)


# In[26]:

for x in a:
       print x,


# The syntax for iteration is...  
# 
#     for variable_name in iterable:
#        # do something with variable_name

# The `range()` function

# In[27]:

x = range(4) ; print x
total = 0
for val in range(4):
        total += val
        print "By adding " + str(val) +               " the total is now " + str(total)


# 
# `range`([`start`,] `stop`[, `step`])
# → list of integers

# In[28]:

total = 0
for val in range(1,10,2):
    total += val
    print "By adding " + str(val) +           " the total is now " + str(total)


# In[29]:

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print i, a[i]


#  &nbsp;

# ### Tuple ###
# denoted with parentheses

# In[30]:

t = (12,-1)
print type(t)


# In[31]:

print isinstance(t,tuple)
print len(t)


# In[32]:

t = (12,"monty",True,-1.23e6)
print t[1]


# In[33]:

print t[-1]


# In[34]:

t[-2:]  # get the last two elements, return as a tuple


# In[35]:

x = (True) ; print type(x)
x = (True,) ; print type(x)


# In[36]:

type(()), len(())


# In[37]:

type((,))


# single-element tuples look like `(element,)`

# cannot change a tuple
# but you can create new one with concatenation

# In[38]:

t[2] = False


# In[39]:

t[0:2], False, t[3:]


# In[40]:

## the above is not what we wanted... need to concatenate
t[0:2] + False + t[3:]


# In[41]:

y = t[0:2] + (False,) + t[3:] ; print y


# In[42]:

t*2


# &nbsp;

# ### Casting Back and Forth ###

# In[43]:

a = [1,2,3,("b",1)]


# In[44]:

b = tuple(a) ; print b


# In[45]:

print list(b)


# In[46]:

set(a)


# In[47]:

list(set("spam"))


# > casting only affects top-level structure, not the elements 

# #### Why use tuples when you have lists? ####

# In[48]:

# A tuple is something that you probably don’t want changed
continents = ("North America", "South America", "Europe", "Asia", "Australia", "Antarctica")

# Something you might want to add and subtract from
tasks = ["learn Python","eat dinner","climb Mt. Everest"] 


# In[49]:

# something you probably don't want in your tasks...
tasks.append("find Atlantis")
print tasks


# In[50]:

# tuples are immutable!
continents.append("Atlantis")


# In[51]:

first_name, last_name = "Jack", "Hewitt" # This is a tuple assignment
print "My name is", first_name, last_name # This statement prints a tuple


# In[52]:

# This function returns a tuple (more on this later…) 
import cmath
r,phi = cmath.polar(-1.); print r,phi


# ### Sets ###
# #### denoted with a curly braces ####

# In[53]:

{1,2,3,"bingo"}


# In[54]:

print type({1,2,3,"bingo"})


# In[55]:

print  type({})


# In[56]:

print type(set())


# In[57]:

set("spamIam")


# sets have unique elements. They can be
# compared, differenced, unionized, etc.

# In[17]:

a = set("sp"); b = set("am"); print a ; print b


# In[18]:

c = set(["a","m"])
c == b


# In[19]:

"p" in a


# In[20]:

"ps" in a


# In[21]:

q = set("spamIam")
a.issubset(q)


# In[22]:

a | b


# In[23]:

q - (a | b)


# In[24]:

q & (a | b)


# Like lists, we can use as (unordered) buckets
# `.pop()` gives us a random element

# In[25]:

# this is pretty volitile...wont be the same
# order on all machines
for i in q & (a | b):
    print i, 


# In[26]:

q.remove("a")


# In[27]:

q.pop()


# In[28]:

print q.pop()
print q.pop()


# In[29]:

print q.pop()


# In[30]:

q.pop()


#  &nbsp;

# ## Dictionaries ##
# denoted with a curly braces and colons

# In[72]:

d = {"favorite cat": None, "favorite spam": "all"}


# these are key: value, key: value, ...

# In[73]:

print d["favorite cat"]
d[0]   ## this is not a list and you dont have a keyword = 0


# In[74]:

e = {"favorite cat": None, "favorite spam": "all",      1: 'loneliest number'}
e[1] == 'loneliest number'


# dictionaries are **UNORDERED**<sup>*</sup>.  
# >You cannot assume that one key comes before or after another
# 
# <sup>*</sup> you can use a special type of ordered dict if you really need it:
# 
# http://docs.python.org/whatsnew/2.7.html#pep-372-adding-an-ordered-dictionary-to-collections

# ### 4 ways to make a Dictionary ###

# In[75]:

# number 1...you've seen this
d = {"favorite cat": None, "favorite spam": "all"}


# In[76]:

# number 2
d = dict(one = 1, two=2,cat = 'dog') ; print d


# In[77]:

# number 3 ... just start filling in items/keys
d = {}  # empty dictionary
d['cat'] = 'dog'
d['one'] = 1
d['two'] = 2
d


# In[78]:

# number 4... start with a list of tuples
mylist = [("cat","dog"), ("one",1),("two",2)]
print dict(mylist)


# In[79]:

dict(mylist) == d


#  &nbsp;

# #### Dictionaries: they can be complicated (in a good way) ####

# In[80]:

d = {"favorite cat": None, "favorite spam": "all"}


# In[81]:

d = {'favorites': {'cat': None, 'spam': 'all'},      'least favorite': {'cat': 'all', 'spam': None}}
print d['least favorite']['cat']


# remember: the backslash (\) allows you to across break lines. Not technically needed when defining a dictionary or list

# In[82]:

phone_numbers = {'family': [('mom','642-2322'),('dad','534-2311')],                     'friends': [('Sylvia','652-2212')]}


# In[83]:

for group_type in ['friends','family']:
        print "Group " + group_type + ":"
        for info in phone_numbers[group_type]:
             print " ",info[0], info[1]


# In[84]:

# this will return a list, but you dont know in what order! 
phone_numbers.keys()


# In[85]:

phone_numbers.values()


#  &nbsp;

# `.keys()` and `.values()`: are called `methods` on dictionaries

# In[86]:

for group_type in phone_numbers.keys():
        print "Group " + group_type + ":"
        for info in phone_numbers[group_type]:
             print " ",info[0], info[1]


# we cannot ensure ordering here of the groups

# In[87]:

groups = phone_numbers.keys()
groups.sort()
for group_type in groups:
        print "Group " + group_type + ":"
        for info in phone_numbers[group_type]:
             print " ",info[0], info[1]


# `.iteritems()` is a handy method,
# returning key,value pairs with each iteration

# In[88]:

for group_type, vals in phone_numbers.iteritems():
        print "Group " + group_type + ":"
        for info in vals:
             print " ",info[0], info[1]


# Some examples of getting values:

# In[89]:

phone_numbers['co-workers']


# In[90]:

phone_numbers.has_key('co-workers')


# In[91]:

print phone_numbers.get('co-workers')


# In[92]:

phone_numbers.get('friends') == phone_numbers['friends']


# In[93]:

print phone_numbers.get('co-workers',"all alone")


#  &nbsp;

# #### setting values ####
# 
# you can edit the values of keys and also `.pop()` & `del` to remove certain keys

# In[94]:

# add to the friends list
phone_numbers['friends'].append(("Jeremy","232-1121"))
print phone_numbers


# In[95]:

## Sylvia's number changed
phone_numbers['friends'][0][1] = "532-1521"


# In[96]:

phone_numbers['friends'][0] = ("Sylvia","232-1521"); 
print phone_numbers['friends']


# In[97]:

## I lost all my friends preparing for this Python class
phone_numbers['friends'] = [] # sets this to an empty list


# In[98]:

## remove the friends key altogether
print phone_numbers.pop('friends')


# In[99]:

print phone_numbers


# In[100]:

del phone_numbers['family']


# In[101]:

print phone_numbers


#  &nbsp;

# `.update()` method is very handy, like `.append()` for lists

# In[102]:

phone_numbers.update({"friends": [("Sylvia's friend, Dave", "532-1521")]})
print phone_numbers


# &nbsp; 

# ## List Comprehension ##
# 
# You can create lists "on the fly" by asking simple questions of other iterateable data structures

# example: I want a list of all numbers from 0 - 100 whose lowest two bits are both one (e.g., 3, 7, ...) but is not divisible by 11

# In[103]:

mylist = []
for num in range(101):
    if (num & 2) and (num & 1) and (num % 11 != 0.0):
        mylist.append(num)
print mylist


# In[104]:

mylist=[num for num in range(101) if (num & 2)         and (num & 1) and (num % 11 != 0.0)]
print mylist


# example: I want a list of all mesons whose masses are between 100 and 1000 MeV

# In[33]:

particles = [{"name":"π+"  ,"mass": 139.57018}, {"name":"π0"  ,"mass": 134.9766}, 
 {"name":"η5"  ,"mass": 47.853}, {"name":"η′(958)","mass": 957.78}, 
 {"name":"ηc(1S)", "mass": 2980.5}, {"name": "ηb(1S)","mass": 9388.9}, 
 {"name":"K+",  "mass": 493.677}, {"name":"K0"  ,"mass": 497.614}, 
 {"name":"K0S" ,"mass":  497.614}, {"name":"K0L" ,"mass":  497.614},
 {"name":"D+"  ,"mass": 1869.62}, {"name":"D0"  ,"mass": 1864.84},
 {"name":"D+s" ,"mass":  1968.49}, {"name":"B+"  ,"mass": 5279.15},
 {"name":"B0"  ,"mass": 5279.5}, {"name":"B0s" ,"mass":  5366.3},
 {"name":"B+c" ,"mass":    6277}]

# data source: http://en.wikipedia.org/wiki/List_of_mesons

my_mesons = [ (x['name'],x['mass']) for     x in particles if x['mass'] <= 1000.0 and x['mass'] >= 100.0]


# In[34]:

# get the average
tot = 0.0
for x in my_mesons: tot += x[1]
print "The average meson mass in this range is " + str(tot/len(my_mesons))     + " MeV/c^2."


# In[35]:

my_mesons[0][0]


# In[36]:

print my_mesons[0][0]


# &nbsp;

# ## Breakout 2##
# Consider the following data detailing Tuesday meetings at Goddard (file: [meetings.py](https://github.com/kialio/python-bootcamp/blob/master/DataFiles_and_Notebooks/02_AdvancedDataStructures/meetings.py)):
# 
#     organizers = { "Extragalactic Journal Club": "Alaina Henry", "Gamma-Ray Burst Lunch": "Judy Racusin", "Astrophysics Colloquium": "Jeremy Schnittman", "Exoplanet Club": "Margaret Pan", "Python Users Group": "Terri Brandt", "IS&T Colloquium Series": "Ben Kobler", "NGAPS Happy Hour": "Toni Venters" }
#             
#     # includes the meeting, room, day, start time(decimal hours), end time
#     meetings = [("Gamma-Ray Burst Lunch","B34 E256","Tue",12.0,13.0),\
#                 ("Extragalactic Journal Club","B34 S391","Tue",14.0,15.0), \
#                 ("Python Users Group","B34 W120A/B","Tue",14.5,15.5), \
#                 ("Astrophysics Colloquium","B34 E215","Tue",15.5,17.0), \
#                 ("NGAPS Happy Hour","B34 E215","Tue",17.0,18.0), \
#                 ("Exoplanet Club","B34 E215","Tue",11.5,12.5), \
#                 ("IS&T Colloquium Series","B3 Auditorium","Tue",11.0,12.0) ]
# 
# 
# Complete the following 2 tasks:
# 
# 1. Print out a schedule organized by meeting name.
# 2. Print out a schedule organized by time. (Hint: You'll need to do a manual sorting on the last element of each flight element, before beginning the printing loop.)
# 
# Example schedule organized by time:
# 
#     Meeting                  		Room No.  	Day	Time 	Organizer
#     -------------------------------------------------------------------------------
#     IS&T Colloquium Series          B3 Auditorium	Tue	11.0 	Ben Kobler
#     Exoplanet Club                  B34 E215     	Tue	11.5 	Margaret Pan
#     Gamma-Ray Burst Lunch           B34 E256     	Tue	12.0 	Judy Racusin
#     ...

# In[38]:

## try it here


# Done? For extra credit: print out a schedule organized by time including meetings on a different day.
# 
#     organizers = { "Extragalactic Journal Club": "Alaina Henry", "Gamma-Ray Burst Lunch": "Judy Racusin",\
#                "Astrophysics Colloquium": "Jeremy Schnittman", "Exoplanet Club": "Margaret Pan",\
#                "Python Users Group": "Terri Brandt", "IS&T Colloquium Series": "Ben Kobler",\
#                "NGAPS Happy Hour": "Toni Venters", "Engineering Colloquium": "Brent Warner", \
#                "SEAL Talk": "Deborah Padgett", "SED Director's Seminar": "Diane Elben", \
#                "Fermi Journal Club": "David Green", "Goddard Scientific Colloquium": "David Thompson" }
# 
#     # includes the meeting, room, day, start time(decimal hours), end time
#     meetings = [("Gamma-Ray Burst Lunch","B34 E256","Tue",12.0,13.0), \
#                 ("Extragalactic Journal Club","B34 S391","Tue",14.0,15.0), \
#                 ("Python Users Group","B34 W120A/B","Tue",14.5,15.5), \
#                 ("Astrophysics Colloquium","B34 E215","Tue",15.5,17.0), \
#                 ("NGAPS Happy Hour","B34 E215","Tue",17.0,18.0), \
#                 ("Exoplanet Club","B34 E215","Tue",11.5,12.5), \
#                 ("Fermi Journal Club","B34 E256","Wed",15.5,16.5),\
#                 ("SEAL Talk","B34 E215","Thu",12.0,13.5), \
#                 ("SED Director's Seminar","B33 H114","Fri",12.0,13.0), \
#                 ("Engineering Colloquium","B3 Auditorium","Mon",15.5,16.5), \
#                 ("Goddard Scientific Colloquium","B3 Auditorium","Fri",15.5,16.5), \
#                 ("IS&T Colloquium Series","B3 Auditorium","Tue",11.0,12.0) ]
# 

# In[39]:

## try it here


# adapted from the UC Berkeley Python Bootcamp by J Bloom
# 
