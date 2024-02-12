"""
C6.24

Describe how to implement the stack ADT using a single queue as an
instance variable, and only constant additional local memory within the
method bodies. What is the running time of the push(), pop(), and top()
methods for your design?

"""

# "An implementation of a deque class is available in python's standard collections module" (6.3.3)
from collections import deque

class StaQue():

    # Constructor
    def __init__(self):
        self.queue = deque()

    # Get the deque length
    def __len__(self):

        return self.queue.__len__()
    
    # check if empty. return true if so
    def is_empty(self):
        
        return self.__len__() == 0

    # add an element to the deque
    def push(self, e):

        # add element to the back
        self.queue.append(e)

        # move all elements to the back
        for i in range(self.__len__() - 1):
            self.queue.append(self.queue.popleft())

    # pop an element out: remove and return the top pointer object
    def pop(self):
        
        # check if its empty
        if self.is_empty():
            raise ValueError('Empty array')
        
        return self.queue.popleft()
    
    # return the reference to the top pointer object, but do not remove it
    def top(self):

        # check if its empty
        if self.is_empty():
            raise ValueError('Empty array')
        
        return self.queue[0]
    
"""
Running time:

push(): O(n)
pop(): O(1)
top(): O(1)

"""

# create a StaQue object
a = StaQue()

# add elements
a.push(1)
a.push(2)
a.push(3)

# get the top element
print(a.top())

# pop off an element
a.pop()

# get the top element again following the pop function call
print(a.top())