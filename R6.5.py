"""
R6.5

Implement a function that reverses a list of elements by pushing them onto
a stack in one order, and writing them back to the list in reversed order.
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

L = [1, 2, 3, 4, 5]

S = ArrayStack()

def reverse_elements(L, S):

    for i in range(0, len(L)):

        v = L.pop()

        S.push(v)
    
    print(S._data, L)

    for i in range(0, S.__len__()):

        L.insert(0, S.pop())

    print(S._data, L) 

reverse_elements(L, S)