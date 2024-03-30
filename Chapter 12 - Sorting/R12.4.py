"""
Is our array-based implementation of merge-sort given in Section 12.2.2
stable? Explain why or why not.
"""

"""
(personal note)
Stable: elements put back based on bucket are put back in the same order as they're found
in the initial sequence, based on keys

Yes. Because for any two entries, K_i and V_i, that preceeds K_j and V_j before sorting,
then they still preceed them after sorting. 
"""

# 12.2.2 merge implementation

def merge(S1, S2, S):

    """Merge two sorted Python lists S1 and S2 into properly sized list S"""

    i = j = 0

    while i + j < len(S):

        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):

            S[i+j] = S1[i]
            i += 1

        else:

            S[i+j] = S2[j]
            j += 1

# 12.2.2 merge-sort implementation

def merge_sort(S):

    """Sort the elements of Python list S using the merge-sort algorithm"""

    n = len(S)

    if n < 2: 
        return # list is already sorted
    
    # Divide
    mid = n // 2
    S1 = S[0:mid]
    S2 = S[mid:n]

    # Conquer
    merge_sort(S1)
    merge_sort(S2)

    merge(S1, S2, S)
