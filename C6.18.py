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

S = ArrayStack()

S.push(1)
S.push(2)
S.push(3)
S.push(4)
S.push(5)

print(S._data)

T = ArrayStack()

def transfer(S, T, U=ArrayStack()):

    print(f'S: {S._data}, T: {T._data}, U: {U._data}')

    if S.is_empty():
        raise ValueError('Stack S is empty')
    
    for i in range(0, S.__len__()):

        T.push(S.pop())

    print(f'S: {S._data}, T: {T._data}, U: {U._data}')

    for i in range(T.__len__()):

        U.push(T.pop())

    print(f'S: {S._data}, T: {T._data}, U: {U._data}')

    for i in range(U.__len__()):

        S.push(U.pop())

    print(f'S: {S._data}, T: {T._data}, U: {U._data}')

transfer(S, T)