"""
R6.1

What values are returned during the following series of stack operations, if
executed upon an initially empty stack? push(5), push(3), pop(), push(2),
push(8), pop(), pop(), push(9), push(1), pop(), push(7), push(6), pop(),
pop(), push(4), pop(), pop().
"""

# stack: LIFO
# push: Add element e to the top of stack S
# pop: Remove and return the top element from the stack S. An error occurs if the stack is empty

def push(S):

    print('this is a sample function so I don\'t get annoying errors below')

def pop():

    print('this is a sample function so I don\'t get annoying errors below')

push(5) #[5]
push(3) #[5, 3]
pop() # [5], returns 3
push(2) # [2, 5]
push(8) # [8, 2, 5]
pop() # [2, 5] returns 8
pop() # [5] returns 2
push(9) # [9, 5]
push(1) # [1, 9, 5]
pop() # [9, 5] returns 1
push(7) # [7, 9, 5]
push(6) # [6, 7, 9, 5]
pop() # [7, 9, 5] returns 6
pop() # [9, 5] returns 7
push(4) # [4, 9, 5] 
pop() # [9, 5] returns 4
pop() # [5] returns 9