import queue

"""
Is our linked-list-based implementation of merge-sort given in Code Frag-
ment 12.3 stable? Explain why or why not.
"""

"""
Yes. Because for the key-value pairs thrown at the methods, they are
put into S in the same order that they appeared in the first place for elements
that are of the same value.
"""

# 12.3 code fragment: L-L implementation of merge-sort

def merge(S1, S2, S):

    """Merge two sorted queue instances S1 and S2 into empty queue S"""

    while not S1.is_empty() and not S2.is_empty():

        if S1.first() < S2.first():
            S.enqueue(S1.dequeue())
        else:
            S.enqueue(S2.dequeue())
    
    while not S1.is_empty():
        S.enqueue(S1.dequeue)
    while not S2.is_empty():
        S.enqueue(S2.dequeue)
    

def merge_sort(S):
    
    """Sort the elements of queue S using the merge-sort algorithm"""
    
    n = len(S)

    if n < 2:
        return
    
    S1 = LinkedQueue()
    S2 = LinkedQueue()

    while len(S1) < n // 2:
        S1.enqueue(S.dequeue())
    while not S.is_empty():
        S2.enqueue(S.dequeue())
    
    merge_sort(S1)
    merge_sort(S2)

    merge(S1, S2, S)

