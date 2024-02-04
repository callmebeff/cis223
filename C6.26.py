"""
C6.26.py

Describe how to implement the double-ended queue ADT using two stacks
as instance variables. What are the running times of the methods?
"""

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

class StaQue():

    # create stacks
    head=ArrayStack()
    tail=ArrayStack()

    DEFAULT_CAPACITY = 10

    
    def __init__(self, head, tail):

        self._size = head.__len__() + tail.__len__()
        self._front = head.top()

    # O(1)
    def __len__(self, head, tail):

        return self._size
    
    # O(1)
    def is_empty(self, head, tail):

        return (head.__len__() == 0 or tail.__len__() == 0)
    

    # O(1)
    # equivalent function for stack is top()
    def first(self, head, tail):

        # if head is empty
        if head.is_empty():
            # if tail is empty, the queue is empty
            if tail.is_empty():
                raise ValueError('Empty queue')
            
            # add the first element of tail into head and return that value
            head.push(tail.pop())

        return head.top()
    # O(1)*
    # dequeue is just popping a value off head
    def dequeue(self, head, tail):

        # if head is empty
        if head.is_empty():
            # if tail is empty, the queue is empty
            if tail.is_empty():
                raise ValueError('Empty queue')
            
            # add the first element of tail into head and return that value
            head.push(tail.pop())

        return head.pop()

    # O(n^2)* :(
    # enqueue is just a push
    def enqueue(self, head, tail, e):

        # if tail is empty, then head is also empty
        if tail.is_empty():
            raise ValueError('Empty array')
        
        # move elements over to head. Otherwise its just added to the middle of the queue (top of tail)
        for i in range(head.__len__()):
            if head.is_empty():
                raise ValueError('Empty array')
            
            for j in range(tail.__len__()):
                head.push(tail.pop)

        # with no elements in tail, add the element. Could optionally move all the elements back over, but this works just fine
        tail.push(e)

"""
Running times:

"""



