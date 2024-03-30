"""
Suppose we are given two n-element sorted sequences A and B each with
distinct elements, but potentially some elements that are in both sequences.
Describe an O(n)-time method for computing a sequence representing the
union A ∪ B (with no duplicates) as a sorted sequence.
"""

"""
You could merge the two lists based on the first element in each array.
Then, you could have a comparison test implemented that will add the 
element of lesser value (or largest, depending on how you want to
sort it). In that scenario, you'd add the lesser value, but there should
also be a check to see if the two are equal. If that's the case, pop
the number from sequence A out into the final sequence, but also pop
that element from sequence B, but don't add it to the final sequence.

"""
