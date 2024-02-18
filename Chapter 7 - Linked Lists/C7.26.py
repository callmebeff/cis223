"""
C7.26

Implement a method, concatenate(Q2) for the LinkedQueue class that
takes all elements of LinkedQueue Q2 and appends them to the end of the
original queue. The operation should run in O(1) time and should result
in Q2 being an empty queue
"""

def concatenate(self, Q2):

    last = self._header
    
    while last._next:
        last = last._next
    
    last._next = Q2._header._next
    Q2._header._next = None
    self._size += Q2._size
    Q2._size = 0