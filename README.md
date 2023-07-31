# Python_practice
Python exercises

Spellchecking python program: 

 It has two input files input.txt and dict.txt and one output file (output.txt). File dict.txt contains a word per line and represents the correct words.
 File input.txt represents a text, written for simplicity with a word per line as well, file output.txt is obtained as follows. For each word, if word is correct
 it is copied to output.txt. If it is not, the program asks the user whether the word should be considered correct. If so, the word is written on output.txt and from now on 
 it becomes the correct word. If not, it asks correct version to the user and the check for correctness restarts.


Needleman Wunsch program: 
The exercise is structured into bullet points, but you should write one single piece of pseudocode including all the parts, and the code you create should be all contained in a single Python script.
1. Define and write a function that takes the following parameters:
	seq1		(the first sequence to be aligned)
	seq2		(the second sequence to be aligned)
	matrix		(a substitution matrix)
	gap			(a gap penalty)

The function should return the score matrix F and the backtracking matrix T necessary to compute the global alignment of the two sequences with the Needleman–Wunsch algorithm

2. Write a main where:

	a) From the file "input_data.py" (the link for downloading it will be provided during the exam), you import the two sequences to align (template, target), the substitution matrix and the gap penalty to adopt (PAM250_dict, gap) and the function to compute the global alignment (backtrack).
	b) Use the function you defined and the one you imported to align the two sequences
	c) Print to the terminal the aligned sequences and the corresponding score in a human-friendly way.
 
