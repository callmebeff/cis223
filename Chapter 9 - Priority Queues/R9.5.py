"""
R9.5

The min method for the UnsortedPriorityQueue class executes in O(n)
time, as analyzed in Table 9.2. Give a simple modification to the class so
that min runs in O(1) time. Explain any necessary modifications to other
methods of the class.

"""

"""
You'd have to have it so that min pulls the first item in the queue, otherwise it has to iterate
through the whole list. I modified the add method to add elements in a sorted manner. Then I
just had to change min to pull the first element in the queue
"""
class PriorityQueueBase:
    """Abstract base class for a priority queue."""

    class Item:
        """Lightweight composite to store priority queue items."""

        slots = '_key' , '_value'
        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            return self._key < other._key # compare items based on their keys

    def is_empty(self): # concrete method assuming abstract len
        """Return True if the priority queue is empty."""
        return len(self) == 0




class UnsortedPriorityQueue(PriorityQueueBase): # base class defines Item
    """A min-oriented priority queue implemented with an unsorted list."""

    def find_min(self): # nonpublic utility
    
        """Return Position of item with minimum key."""
        if self.is_empty(): # is empty inherited from base class
            raise ValueError( 'Priority queue is empty' )
        small = self._data.first()
        walk = self._data.after(small)
        while walk is not None:
            if walk.element() < small.element():
                small = walk
                walk = self._data.after(walk)
        return small

    def __init__(self):
        """Create a new empty Priority Queue."""
        self._data = PositionalList()

    def __len__(self):
        """Return the number of items in the priority queue."""
        return len(self._data)

    def add(self, key, value):
        """Add a key-value pair."""
        # self._data.add_last(self._Item(key, value))

        newest = self._Item(key, value)
        walk = self._data.last()
        while walk is not None and newest < walk.element():
            walk = self._data.before(walk)

        if walk is None:
            self._data.add_first(newest)
        else:
            self._data.add_after(walk, newest)


    def min(self):
        """Return but do not remove (k,v) tuple with minimum key."""
        p = self._data.first()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key."""
        p = self._find_min()
        item = self._data.delete(p)
        return (item._key, item._value)