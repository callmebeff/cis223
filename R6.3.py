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

    # constructor
    def __init__(self):

        self._data = []

    # get the length of the stack
    def __len__(self):

        return len(self._data)
    
    # check if the stack is empty
    def is_empty(self):

        if len(self._data) == 0:
            return True
        else:
            return False
    
    # add an element to the stack
    def push(self, e):

        self._data.append(e)

    # return the reference to the first object but do not remove it from the stack
    def top(self):

        if self._data.is_empty():
            raise ValueError('Stack is empty')
        
        return self._data[-1]

    # return the reference to the first object and remove it from the stack
    def pop(self):

        if self.is_empty():
            raise ValueError('Stack is empty')
        
        return self._data.pop()

# transfer elements to another stack, putting them into the other stack in reverse order
def signature_transfer(S, T):

    if S.is_empty():
        raise ValueError('Stack S is empty')
    
    # iterate through the elements in S
    for i in range(0, S.__len__()):

        # pop the elements out of S and add them to T
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