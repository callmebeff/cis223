"""
R6.13

Suppose you have a deque D containing the numbers (1, 2, 3, 4, 5, 6, 7, 8),
in this order. Suppose further that you have an initially empty queue Q.
Give a code fragment that uses only D and Q (and no other variables) and
results in D storing the elements in the order (1, 2, 3, 5, 4, 6, 7, 8).
"""

class ArrayQueue():

    DEFAULT_CAPACITY = 10

    def __init__(self):

        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

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
            self._resize(2 * len(self.data)) # Double the array size

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

# queue to dequeue
D = ArrayQueue()

# add elements
D.enqueue(1)
D.enqueue(2)
D.enqueue(3)
D.enqueue(4)
D.enqueue(5)
D.enqueue(6)
D.enqueue(7)
D.enqueue(8)

# queue to enqueue
Q = ArrayQueue()

# initial queue values
print(f'--initial--\nQueue D: {D._data}\nQueue Q: {Q._data}')

# iterate through queue D
for i in range(D.__len__()):
    
    # dequeue each element in D and queue it into Q
    Q.enqueue(D.dequeue())

# final queue values
print(f'--final--\nQueue D: {D._data}\nQueue Q: {Q._data}')

