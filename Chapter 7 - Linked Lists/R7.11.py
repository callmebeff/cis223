"""
R7.11

Implement a function, with calling syntax max(L), that returns the max-
imum element from a PositionalList instance L containing comparable
elements.
"""

def max(L):

    element = L._header._next
    max_element = element._element

    while(element._next):
        if max_element < element._element:
            max_element = element._element

        element = element._next
    return max_element
            