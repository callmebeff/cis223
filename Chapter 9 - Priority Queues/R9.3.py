"""
R9.3

What does each remove min call return within the following sequence of
priority queue ADT methods: add(5,A), add(4,B), add(7,F), add(1,D),
remove min( ), add(3,J), add(6,L), remove min( ), remove min( ),
add(8,G), remove min( ), add(2,H), remove min( ), remove min( )?
"""

"""
add(5,A)
[5:A]
add(4,B)
[4:B, 5:A]
add(7,F)
[4:B, 5:A, 7:F]
add(1,D)
[1:D, 4:B, 5:A, 7:F]
remove min( )
Removes & returns 1:D
add(3,J)
[3:J, 4:B, 5:A, 7:F]
add(6,L)
[3:J, 4:B, 5:A, 6:L, 7:F]
remove min( )
Removes & returns 3:J
remove min( )
Removes 4:B
add(8,G)
[5:A, 6:L, 7:F, 8:B]
remove min( )
Removes 5:A
add(2,H)
[2: H, 6:L, 7:F, 8:B]
remove min( )
Removes 2:H
remove min( )
Removes 6:L


"""