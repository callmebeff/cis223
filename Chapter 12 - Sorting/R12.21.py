"""
Given a sequence S of n values, each equal to 0 or 1, describe an in-place
method for sorting S.
"""

"""
(personal note)
In-place algorithm: An in-place algorithm is an algorithm that does not need an extra space and produces 
an output in the same memory that contains the data by transforming the input 'in-place'. However, 
a small constant extra space used for variables is allowed.
"""

def inplace(S, a, b): # a: leftmost index. b: rightmost index

    if a >= b: return

    pivot = S[b]
    left = a
    right = b-1

    while left <= right:

        # scan until reaching value equal or larger than pivot or right marker
        while left <= right and S[left] < pivot:
            left += 1
        # scan until reaching value equal or smaller than pivot
        while left <= right and pivot < S[right]:
            right -= 1
        if left <= right:
            S[left], S[right] = S[right], S[left]
        left, right = left + 1, right - 1

    S[left], S[b] = S[b], S[left]

    inplace(S, a, left - 1)
    inplace(S, left + 1, b)
