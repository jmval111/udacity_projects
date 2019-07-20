### Problem 3 - Huffman Node

#### Reasoning:
For this problem, I chose to implement the solution using a custom object called a HuffmanTree().  This object is used to produce a tree using the character frequencies.  This object calculates the frequencies, builds the tree, makes the codes, and decodes the message.


#### Efficiency:
* Time efficiency - O(n log n) worst case.  The array used as a heap in this code must be sorted each time after two nodes are extracted and combined.  This array is a native python structure that uses O(n log n) time.  All other functions use O(n) time.
* Space efficiency - O(n) worst case, where n is the number of unique characters in the input data.

