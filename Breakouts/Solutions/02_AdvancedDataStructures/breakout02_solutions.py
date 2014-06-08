
# coding: utf-8

# <p class="title">Breakout 2 Solutions</p>
# 
# <p class="subtitle">Sorting meetings</p>
# 
# <center>
# 
# <p class="gap05"><p>
# <h3>Python Boot Camp</h3>
# <h3>June 9, 2014</h3>
# 
# 
# </center>
# 
# 
# 
# 

# 
# ### First, copy over the meeting and organizer information from [meetings.py](https://github.com/kialio/python-bootcamp/blob/master/DataFiles_and_Notebooks/02_AdvancedDataStructures/meetings.py). ###

# In[5]:

organizers = { "Extragalactic Journal Club": "Alaina Henry", "Gamma-Ray Burst Lunch": "Judy Racusin",               "Astrophysics Colloquium": "Jeremy Schnittman", "Exoplanet Club": "Margaret Pan",               "Python Users Group": "Terri Brandt", "IS&T Colloquium Series": "Ben Kobler",               "NGAPS Happy Hour": "Toni Venters" }


# In[6]:

# meeting, room, day, start time(decimal hours), end time
meetings = [("Gamma-Ray Burst Lunch","B34 E256","Tue",12.0,13.0),             ("Extragalactic Journal Club","B34 S391","Tue",14.0,15.0),             ("Python Users Group","B34 W120A/B","Tue",14.5,15.5),             ("Astrophysics Colloquium","B34 E215","Tue",15.5,17.0),             ("NGAPS Happy Hour","B34 E215","Tue",17.0,18.0),             ("Exoplanet Club","B34 E215","Tue",11.5,12.5),             ("IS&T Colloquium Series","B3 Auditorium","Tue",11.0,12.0) ]


# <h2>Sorting by Meeting Name</h2>
# ### We can sort the meeting information by meeting name by running a simple sort on the list. ###
# 

# In[7]:

# Sort the list of meetings.
meetings.sort() 


# When we called flights.sort() we resorted the list based on the first element of each tuple (airline) and then, when multiple flights are operated by one ariline, by the flight number.

# In[8]:

for meeting in meetings:
    print meeting


# <h2>Printing the list</h2>
# ###Now we want to print out the sorted list in a nicer format.###
# 
# Note that when printing, we lookup the destination name by the airport code key in the airports dictionary.

# In[9]:

# Print out the header. the \t character prints a tab.
print "Meeting          \t\tRoom No.\tDay\tTime\tOrganizer"
print "-"*81 #81 instances of the "-" character

# Loop through each of the flight tuples in the sorted list
# Recall that each tuple contains the elements: (airline, number, destination lookup code, gate, time)
for meeting in meetings:
    # Use the meeting name to lookup the organizer's name from the organizers directory
    talk_name = meeting[0]
    talk_name += " "*(32 - len(meeting[0]))  # add the appropriate amount of whitespace after the Destination string
    organizer = organizers[meeting[0]]
    organizer += " "*(10 - len(organizer))  # add the appropriate amount of whitespace after the Destination string
    # Print the nicely formatted string. Don't forget to convert int and float types to strings using str()
    print talk_name + str(meeting[1]) + "\t" + str(meeting[2]) + "\t" + str(meeting[3]) + "\t" + organizer 


# <h2>Sorting by Meeting Time</h2>
# ### Sorting the information by time requires a bit more coding. ###
# First, we create a new list, time_ordered_meetings, which initially just contains the first element of the list meetings.

# In[10]:

# Create a new list, time_ordered, which initially just contains the first element of the list flights
time_ordered_meetings = [meetings[0]]
print time_ordered_meetings


# It's easy to loop through the remaining meetings and insert them into the propoer position in time_ordered_meetings by comparing the day in each meeting tuple (at the fourth index position).
# 
# We determine where the current meeting belongs by manually comparing the time of the meeting already added to time_ordered_meetings. (This is really trivial with lambda functions, which you'll learn later.)

# In[11]:

# Iterate through each of the remaining elements in flights to see where it should go in the sorted list
for meeting in meetings[1:]:
    # Does it belong in the beginning?
    if meeting[3] < time_ordered_meetings[0][3]: #is the day of the meeting before the first list element?
      time_ordered_meetings.insert(0,meeting)  # insert the meeting tuple at position 0 in the list 
      continue
    ## ... or the end?
    if meeting[3] > time_ordered_meetings[-1][2]: #is the day of the meeting after the first list element?
      time_ordered_meetings.append(meeting)  # insert the meeting tuple at the end of the list
      continue
    ## Or is it in the middle? Loop through each day to see if the current meeting is between two adjacent ones
    ## note that range(N) returns a list [0, 1, ... , N-1] 
    for i in range(len(time_ordered_meetings) - 1): 
        if meeting[3] >= time_ordered_meetings[i][3] and meeting[3] <= time_ordered_meetings[i+1][3]:
            time_ordered_meetings.insert(i+1,meeting) # insert the flight tuple at position i+1 in the list
            break


# The printing procedure is the same as before.

# In[12]:

print "Meeting          \t\tRoom No.\tDay\tTime\tOrganizer"
print "-"*81 #81 instances of the "-" character
for meeting in time_ordered_meetings:
    # Use the meeting name to lookup the organizer's name from the organizers directory
    talk_name = meeting[0]
    talk_name += " "*(32 - len(meeting[0]))  # add the appropriate amount of whitespace after the Destination string
    organizer = organizers[meeting[0]]
    organizer += " "*(10 - len(organizer))  # add the appropriate amount of whitespace after the Destination string
    # Print the nicely formatted string. Don't forget to convert int and float types to strings using str()
    print talk_name + str(meeting[1]) + "\t" + str(meeting[2]) + "\t" + str(meeting[3]) + "\t" + organizer 


# ### One line sorting solution. ###
# We can use the operator.itemgetter() function as the key in sort and sort by the time (4th) element.

# In[15]:

import operator
meetings.sort(key=operator.itemgetter(3))

print "Meeting          \t\tRoom No.\tDay\tTime\tOrganizer"
print "-"*81 #81 instances of the "-" character
for meeting in meetings:
    talk_name = meeting[0]
    talk_name += " "*(32 - len(meeting[0]))
    organizer = organizers[meeting[0]]
    organizer += " "*(10 - len(organizer))
    print talk_name + str(meeting[1]) + "\t" + str(meeting[2]) + "\t" + str(meeting[3]) + "\t" + organizer 


# ###Alternate printing solution###
# Define how many spaces you want each string to occupy. Add enough trailing spaces to each element to fill this number. We'll go over string formatting more tomorrow. 

# In[24]:

print "%.27s %.14s %.4s %.5s %.20s" % ("Meeting"+27*' ', "Room No."+14*' ', "Day"+4*' ', "Time"+5*' ', "Organizer"+20*' ')
print "-"*72
for meeting in meetings:
    print "%.27s %.14s %.4s %.5s %.20s" % (meeting[0]+27*' ', meeting[1]+14*' ', meeting[2]+4*' ',                                           str(meeting[3])+5*' ', organizers[meeting[0]]+20*' ')


# ###Extra Credit###
# What if we had meetings on other days of the week? How would we sort our meetings by both day of the week and time? (The one-liner solution comes tomorrow.)

# In[25]:

organizers = { "Extragalactic Journal Club": "Alaina Henry", "Gamma-Ray Burst Lunch": "Judy Racusin",               "Astrophysics Colloquium": "Jeremy Schnittman", "Exoplanet Club": "Margaret Pan",               "Python Users Group": "Terri Brandt", "IS&T Colloquium Series": "Ben Kobler",               "NGAPS Happy Hour": "Toni Venters", "Engineering Colloquium": "Brent Warner",                "Fermi Journal Club": "David Green", "Goddard Scientific Colloquium": "David Thompson" }

# meeting, room, day, start time(decimal hours), end time
meetings = [("Gamma-Ray Burst Lunch","B34 E256","Tue",12.0,13.0),             ("Extragalactic Journal Club","B34 S391","Tue",14.0,15.0),             ("Python Users Group","B34 W120A/B","Tue",14.5,15.5),             ("Astrophysics Colloquium","B34 E215","Tue",15.5,17.0),             ("NGAPS Happy Hour","B34 E215","Tue",17.0,18.0),             ("Exoplanet Club","B34 E215","Tue",11.5,12.5),             ("Fermi Journal Club","B34 E256","Wed",15.5,16.5),            ("Engineering Colloquium","B3 Auditorium","Mon",15.5,16.5),             ("Goddard Scientific Colloquium","B3 Auditorium","Fri",15.5,16.5),             ("IS&T Colloquium Series","B3 Auditorium","Tue",11.0,12.0) ]


# In[32]:

days_of_week=('Mon','Tue','Wed','Thu','Fri')
meetings.sort(key=operator.itemgetter(3))
meetings2 = [(meeting[0], meeting[1], meeting[2], meeting[3], meeting[4], days_of_week.index(meeting[2]) ) for meeting in meetings]
meetings2.sort(key=operator.itemgetter(5))
print "%.27s %.14s %.4s %.5s %.20s" % ("Meeting"+27*' ', "Room No."+14*' ', "Day"+4*' ', "Time"+5*' ', "Organizer"+20*' ')
print "-"*72
for meeting in meetings2:
    print "%.27s %.14s %.4s %.5s %.20s" % (meeting[0]+27*' ', meeting[1]+14*' ', meeting[2]+4*' ',                                           str(meeting[3])+5*' ', organizers[meeting[0]]+20*' ')

