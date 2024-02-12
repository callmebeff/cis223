"""
R6.14

Repeat the previous problem using the deque D and an initially empty
stack S.
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


class ArrayStack():

    def __init__(self):

        self._data = []

    def __len__(self):

        return len(self._data)
    
    def is_empty(self):

        if len(self._data) == 0:
            return True
        else:
            return False
        
    def push(self, e):

        self._data.append(e)

    def top(self):

        if self._data.is_empty():
            raise ValueError('Stack is empty')
        
        return self._data[-1]

    def pop(self):

        if self.is_empty():
            raise ValueError('Stack is empty')
        
        return self._data.pop()

# create queue
D = ArrayQueue()

# queue elements
D.enqueue(1)
D.enqueue(2)
D.enqueue(3)
D.enqueue(4)
D.enqueue(5)
D.enqueue(6)
D.enqueue(7)
D.enqueue(8)

# create stacj
S = ArrayStack()

print(f'--initial--\nQueue D: {D._data}\nStack S: {S._data}')

# iterate through queue D
for i in range(D.__len__()):
    
    # for each element dequeued from D, add it to stack S
    S.push(D.dequeue())

print(f'--final--\nQueue D: {D._data}\nStack S: {S._data}')
