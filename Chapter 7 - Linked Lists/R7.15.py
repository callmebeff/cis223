"""
R7.15

Provide support for a __reversed__ method of the PositionalList class that
is similar to the given iter , but that iterates the elements in reversed
order.
"""

def __reversed__(self):

    cursor = self.last()
    while cursor:
        yield cursor.element()
        cursor = self.before(cursor)