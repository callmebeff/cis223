"""
R13.11

Draw the frequency array and Huffman tree for the following string:
"dogs do not spot hot pots or cats".

"""

s = "dogs do not spot hot pots or cats"

unique_letters = ['d', 'o', 'g', 's', 'n', 't', 'p', 'h', 'r', 'c', 'a']

letter_count = [2, 7, 1, 4, 1, 5, 2, 1, 1, 1, 1]

for i in range(len(unique_letters)):
        
    print(f'Letter: {unique_letters[i]}')
    print(f'Freq: {letter_count[i]}')

