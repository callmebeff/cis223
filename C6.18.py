"""
R6.18

Show how to use the transfer function, described in Exercise R-6.3, and
two temporary stacks, to replace the contents of a given stack S with those
same elements, but in reversed order.

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

# create stack S
S = ArrayStack()

# add elements to stack
S.push(1)
S.push(2)
S.push(3)
S.push(4)
S.push(5)



def transfer(S):

    # temporary stacks
    T = ArrayStack()
    U=ArrayStack()

    # initial run
    print(f'--initial--\nS: {S._data}\nT: {T._data}\nU: {U._data}')

    # make sure S is not empty
    if S.is_empty():
        raise ValueError('Stack S is empty')
    
    # iterate through S
    for i in range(0, S.__len__()):

        # pop element and add it into T. This will put the elements in reverse order
        T.push(S.pop())

    print(f'--next--\nS: {S._data}\nT: {T._data}\nU: {U._data}')

    # iterate through T
    for i in range(T.__len__()):

        # pop element from T and add it to U. This will put elements in reverse order of T, but in the correct initial order of S
        U.push(T.pop())

    print(f'--next--\nS: {S._data}\nT: {T._data}\nU: {U._data}')

    # iterate through U
    for i in range(U.__len__()):

        # pop element from U and add it to S. elements will be added in reverse order of U, which was the correct intial order of S, thereby reversing S's initial order of elements
        S.push(U.pop())

    print(f'--final--\nS: {S._data}\nT: {T._data}\nU: {U._data}')

transfer(S)