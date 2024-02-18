"""
R7.3

Describe a recursive algorithm that counts the number of nodes in a singly
linked list
"""

"""
A recursive algorithm that counts the number of nodes in a singly linked list would take in a list, and have a check to see if the list is empty.
If the list is empty, then return that it's empty. If its not, pop off an element, store it, and increase the count. Then run the list through
again minus the popped element, and do the same thing. Eventually, return the sum of the counters back to the top, then you get the number of nodes.
"""