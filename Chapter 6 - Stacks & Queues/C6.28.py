"""
C6.28

Modify the ArrayQueue implementation so that the queue’s capacity is
limited to maxlen elements, where maxlen is an optional parameter to the
constructor (that defaults to None). If enqueue is called when the queue
is at full capacity, throw a Full exception (defined similarly to Empty).
"""

class ArrayQueue():

    def __init__(self, maxlen=None):

        self._data = [None] * maxlen
        self._size = 0
        self._front = 0
        self.maxlen = maxlen

    def __len__(self):

        return self._size
    
    def is_empty(self):

        return self._size == 0
    
    def first(self):

        if self.is_empty():
            raise ValueError('Queue is empty.')
        
        return self._data[self._front]
    
    def dequeue(self):

        if self.is_empty():
            raise ValueError('Queue is empty')
        
        answer = self._data[self._front]

        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1

        return answer
    
    def enqueue(self, e):

        if self._size ==len(self._data):

            raise ValueError('Queue is full.')

        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def resize(self, cap):

        old = self._data
        self._data = None * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0
