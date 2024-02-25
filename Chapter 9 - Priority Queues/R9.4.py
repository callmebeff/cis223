"""
R9.4

An airport is developing a computer simulation of air-traffic control that
handles events such as landings and takeoffs. Each event has a time stamp
that denotes the time when the event will occur. The simulation program
needs to efficiently perform the following two fundamental operations:

• Insert an event with a given time stamp (that is, add a future event).

• Extract the event with smallest time stamp (that is, determine the next event to process).

Which data structure should be used for the above operations? Why?

"""

"""
A sorted priority queue would be best because it'd arrange the timing of planes landing in sequential order, allocating the landing strip to a 
given plane based on when it lands (its priority)

"""