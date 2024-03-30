"""
Describe and analyze an efficient method for removing all duplicates from
a collection A of n elements.
"""

"""
First, sort the collection using a quick sort algorithm, which runs in O(nlogn) Then, you can iterate 
through, keeping a variable set to be equal to a given element, and another one that is set to equal to 
the element that follows it in the array. If at any point these two are equal, remove one of those elements.
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