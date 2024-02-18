"""
R7.7

Our CircularQueue class of Section 7.2.2 provides a rotate( ) method that
has semantics equivalent to Q.enqueue(Q.dequeue( )), for a nonempty
queue. Implement such a method for the LinkedQueue class of Sec-
tion 7.1.2 without the creation of any new nodes
"""

class CircularQueue():

    class _Node():
        
        # Lightweight, nonpublic class for storing a singly linked node.

        __slots__ = '_element', '_next' # streamline memory usage

        def __init__(self, element, next=None): # initialize node’s fields

            self._element = element # reference to user’s element
            self._next = next # reference to next node
    
    def __init__(self):

        self._tail = None
        self._size = 0

    def __len__(self):

        return self._size
    
    def is_empty(self):

        return self._size == 0
    
    def first(self):

        if self.is_empty():
            raise ValueError('Queue is empty')
        
        head = self._tail._next
        return head._element
    
    def dequeue(self):

        if self.is_empty():
            raise ValueError('Queue is empty')
        
        oldhead = self._tail._next
        if self._size == 1:
            self._tail = None

        else:
            self._tail = oldhead._next

        self._size -= 1
        return oldhead._element
    
    def enqueue(self, e):

        newest = self._Node(e, None)
        if self.is_empty():
            raise ValueError('Empty')
        
        else:
            newest._next = newest
            self._tail._next = newest

        self._tail = newest
        self._size += 1

    def rotate(self):

        if self.is_empty():
            raise ValueError('Empty queue')
        
        self._tail = self._tail._next
