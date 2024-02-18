"""
R7.2

Describe a good algorithm for concatenating two singly linked lists L and
M, given only references to the first node of each list, into a single list L_prime
that contains all the nodes of L followed by all the nodes of M
"""

#-------------------------- nested Node class --------------------------
class Node():
    
    # Lightweight, nonpublic class for storing a singly linked node.

    __slots__ = '_element', '_next' # streamline memory usage

    def __init__(self, element, next=None): # initialize node’s fields

        self._element = element # reference to user’s element
        self._next = next # reference to next node


class LinkedList():

    #initialize head
    def __init__(self):
        
        self._head = None

    def print_list(self):

        temp = self._head

        while temp:
            print(temp._element)
            temp = temp._next

L = LinkedList()
L._head = Node(0)
L_second = Node(1)
L_third = Node(2)

L._head._next = L_second
L_second._next = L_third

M = LinkedList()
M._head = Node(3)
M_second = Node(4)
M_third = Node(5)

M._head._next = M_second
M_second._next = M_third


a = L._head

while(a._next):

    a = a._next

a._next = M._head

N = L

N.print_list()