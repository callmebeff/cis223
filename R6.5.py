"""
R6.5

Implement a function that reverses a list of elements by pushing them onto
a stack in one order, and writing them back to the list in reversed order.
"""

class ArrayStack():

    # constructor
    def __init__(self):

        self._data = []

    # stack length
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

    # return the reference to the top object in the stack
    def top(self):

        if self._data.is_empty():
            raise ValueError('Stack is empty')
        
        return self._data[-1]

    # return the reference to the top object in the stack but do not remove it
    def pop(self):

        if self.is_empty():
            raise ValueError('Stack is empty')
        
        return self._data.pop()

# list to reverse
L = [1, 2, 3, 4, 5]

# stack
S = ArrayStack()

# function to reverse the elements
def reverse_elements(L, S):

    print(f'--initial--\nStack S: {S._data}\n List L: {L}') 

    # iterate through the list
    for i in range(0, len(L)):
        
        # pop each element out and add it to the stack S
        S.push(L.pop())
    
    # puts it into the stack in reverse order
    print(f'--next--\nStack S: {S._data}\n List L: {L}') 

    # iterate through stack S
    for i in range(0, S.__len__()):

        # insert, to the front, the elements popped out of stack S
        L.insert(0, S.pop())

    # show that the elements have been reversed
    print(f'--final--\nStack S: {S._data}\n List L: {L}') 

reverse_elements(L, S)