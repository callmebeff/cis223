import random

questions = [

    "R6.18: Show how to use the transfer function, described in Exercise R-6.3, and two temporary stacks, to replace the contents of a given stack S with those same elements, but in reversed order.",
    "C6.24:  Describe how to implement the stack ADT using a single queue as an instance variable, and only constant additional local memory within the method bodies. What is the running time of the push(), pop(), and top() methods for your design?",
    "C6.26:  Describe how to implement the double-ended queue ADT using two stacks as instance variables. What are the running times of the methods?",
    "C6.28:  Modify the ArrayQueue implementation so that the queue’s capacity is limited to maxlen elements, where maxlen is an optional parameter to the constructor (that defaults to None). If enqueue is called when the queue is at full capacity, throw a Full exception (defined similarly to Empty).",
    "R6.1 : What values are returned during the following series of stack operations, if executed upon an initially empty stack? push(5), push(3), pop(), push(2), push(8), pop(), pop(), push(9), push(1), pop(), push(7), push(6), pop(), pop(), push(4), pop(), pop().",
    "R6.2 : Suppose an initially empty stack S has executed a total of 25 push operations, 12 top operations, and 10 pop operations, 3 of which raised Empty errors that were caught and ignored. What is the current size of S?",
    "R6.3 : Implement a function with signature transfer(S, T) that transfers all ele- ments from stack S onto stack T, so that the element that starts at the top of S is the first to be inserted onto T, and the element at the bottom of S ends up at the top of T ",
    "R6.5 : Implement a function that reverses a list of elements by pushing them onto a stack in one order, and writing them back to the list in reversed order.",
    "R6.7 : What values are returned during the following sequence of queue opera- tions, if executed on an initially empty queue? enqueue(5), enqueue(3), dequeue(), enqueue(2), enqueue(8), dequeue(), dequeue(), enqueue(9), enqueue(1), dequeue(), enqueue(7), enqueue(6), dequeue(), dequeue(), enqueue(4), dequeue(), dequeue().",
    "R6.8 : Suppose an initially empty queue Q has executed a total of 32 enqueue operations, 10 first operations, and 15 dequeue operations, 5 of which raised Empty errors that were caught and ignored. What is the current size of Q?",
    "R6.13:  Suppose you have a deque D containing the numbers (1, 2, 3, 4, 5, 6, 7, 8), in this order. Suppose further that you have an initially empty queue Q. Give a code fragment that uses only D and Q (and no other variables) and results in D storing the elements in the order (1, 2, 3, 5, 4, 6, 7, 8).",
    "R6.14:  Repeat the previous problem using the deque D and an initially empty stack S.",
    "C7.26:  Implement a method, concatenate(Q2) for the LinkedQueue class that takes all elements of LinkedQueue Q2 and appends them to the end of the original queue. The operation should run in O(1) time and should result in Q2 being an empty queue",
    "R7.2 : Describe a good algorithm for concatenating two singly linked lists L and M, given only references to the first node of each list, into a single list L_prime that contains all the nodes of L followed by all the nodes of M",
    "R7.3 : Describe a recursive algorithm that counts the number of nodes in a singly linked list",
    "R7.7 : Our CircularQueue class of Section 7.2.2 provides a rotate( ) method that has semantics equivalent to Q.enqueue(Q.dequeue( )), for a nonempty queue. Implement such a method for the LinkedQueue class of Sec- tion 7.1.2 without the creation of any new nodes",
    "R7.11:  Implement a function, with calling syntax max(L), that returns the max- imum element from a PositionalList instance L containing comparable elements.",
    "R7.13:  Update the PositionalList class to support an additional method find(e), which returns the position of the (first occurrence of ) element e in the list (or None if not found).",
    "R7.15:  Provide support for a __reversed__ method of the PositionalList class that is similar to the given iter , but that iterates the elements in reversed order.",
    "R8.7 : What are the minimum and maximum number of internal and external nodes in an improper binary tree with n nodes?",
    "R8.10: Give a direct implementation of the num children method within the class BinaryTree."
    "R8.20: Draw a binary tree T that simultaneously satisfies the following: • Each internal node of T stores a single character. • A preorder traversal of T yields EXAMFUN. • An inorder traversal of T yields MAFXUEN.",
    "C8.34: For a tree T , let nI denote the number of its internal nodes, and let nE denote the number of its external nodes. Show that if every internal node in T has exactly 3 children, then nE = 2nI + 1.",
    "C8.60: Suppose each position p of a binary tree T is labeled with its value f (p) in a level numbering of T . Design a fast method for determining f (a) for the lowest common ancestor (LCA), a, of two positions p and q in T , given f (p) and f (q). You do not need to find position a, just value f (a).",
    "CH8P6a",
    "CH8P6b",
    "CH8P7a",
    "CH8P7b",
    "CH8P8a",
    "CH8P8b",
    "R9.2  Suppose you label each position p of a binary tree T with a key equal to its preorder rank. Under what circumstances is T a heap?",
    "R9.3  What does each remove min call return within the following sequence of priority queue ADT methods: add(5,A), add(4,B), add(7,F), add(1,D), remove min( ), add(3,J), add(6,L), remove min( ), remove min( ), add(8,G), remove min( ), add(2,H), remove min( ), remove min( )?",
    "R9.4  An airport is developing a computer simulation of air-traffic control thathandles events such as landings and takeoffs. Each event has a time stampthat denotes the time when the event will occur. The simulation programneeds to efficiently perform the following two fundamental operations:• Insert an event with a given time stamp (that is, add a future event).• Extract the event with smallest time stamp (that is, determine the next event to process).Which data structure should be used for the above operations? Why?",
    "R9.5  The min method for the UnsortedPriorityQueue class executes in O(n) time, as analyzed in Table 9.2. Give a simple modification to the class so that min runs in O(1) time. Explain any necessary modifications to other methods of the class.",
    "R9.6  Can you adapt your solution to the previous problem to make remove min run in O(1) time for the UnsortedPriorityQueue class? Explain your an- swer",
    "R9.10 At which positions of a heap might the third smallest key be stored?",
    "R9.11 At which positions of a heap might the largest key be stored?",
    "R9.17  Let H be a heap storing 15 entries using the array-based representation of a complete binary tree. What is the sequence of indices of the array that are visited in a preorder traversal of H? What about an inorder traversal of H? What about a postorder traversal of H"

]

print(f'\n{random.choice(questions)}\n')