"""
R6.3

Implement a function with signature transfer(S, T) that transfers all ele-
ments from stack S onto stack T, so that the element that starts at the top
of S is the first to be inserted onto T, and the element at the bottom of S
ends up at the top of T

BOOK: 6.1.3
"""

# Building ArrayStack Class
# Requires constructor, __len__, is_empty, push(), top(), and pop()

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
    
def signature_transfer(S, T):

    if S.is_empty():
        raise ValueError('Stack S is empty')
    
    for i in range(0, S.__len__()):

        T.push(S.pop())

 

S = ArrayStack()

S.push(1)
S.push(2)
S.push(3)
S.push(4)
S.push(5)

T = ArrayStack()

signature_transfer(S, T)

print(T._data)