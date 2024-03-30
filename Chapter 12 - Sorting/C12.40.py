"""
Let S1, S2, . . . , Sk be k different sequences whose elements have integer
keys in the range [0, N-1], for some parameter N ≥ 2. Describe an algo-
rithm that produces k respective sorted sequences in O(n + N) time, where*
n denotes the sum of the sizes of those sequences.
"""

"""
Since the range of the amount of sequences is defined, we can implement
a bucket sort, which would split each of those sequences up into an
amount k of sorted sequences. This would ultimately include two
independant loops and a defined amount of buckets for each value
in each sequence. Resulting from this, we would obtain a total size 
of O(n + N) for this algorithm.
"""