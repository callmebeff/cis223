"""
R7.13

Update the PositionalList class to support an additional method find(e),
which returns the position of the (first occurrence of ) element e in the list
(or None if not found).
"""

def find(self, e):

    n = self._first()
    while (self._after(n)):

        if n._element() == e:
            return n
        
        n = self.after(n)

    return None