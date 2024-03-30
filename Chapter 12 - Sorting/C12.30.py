import random

"""
Modify our in-place quick-sort implementation of Code Fragment 12.6 to
be a randomized version of the algorithm, as discussed in Section 12.3.1.
"""

def inplace_quick_sort(S, a, b): # a: leftmost index. b: rightmost index

    if a >= b: return

    pivot = S[random.randint(0, len(S)-1)]
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

    inplace_quick_sort(S, a, left - 1)
    inplace_quick_sort(S, left + 1, b)