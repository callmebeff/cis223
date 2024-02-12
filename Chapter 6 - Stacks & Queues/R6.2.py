"""
R6.2

Suppose an initially empty stack S has executed a total of 25 push operations,
12 top operations, and 10 pop operations, 3 of which raised Empty
errors that were caught and ignored. What is the current size of S?
"""

S = []

# push 25 times, adding elements to the array:

[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

# top 12 times, returns a reference to the top element of stack S without removing it. An error occurs if the stack is empty

[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

# 10 pop operations

[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

# 3 of which raised empty errors, which were ignored

[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]

"""
The stack should be a length of 17, or in other words, has 18 elements
"""
