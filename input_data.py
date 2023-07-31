'''
2) Write the pseudocode on paper, when you are done with the paper part of BOTH the exercises write it on the computer (you cannot touch the paper part anymore). Debug it. Send the final Python code to allegra.via@gmail.com & matteo.manfredi4@unibo.it (use a .txt extension because Outlook blocks files with a .py extension)
Pseudocode and code are expected to be roughly aligned (except for minor deviations)

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
'''


def backtrack(seq1, seq2, F, T):
	aln1, aln2 = '', ''
	i , j = len(seq2), len(seq1)
	
	while T[i][j] != 'end':
		if T[i][j] == 'd':
			#We are matching
			aln1 = seq1[j-1] + aln1
			aln2 = seq2[i-1] + aln2
			i -= 1
			j -= 1	#Move diagonally
		elif T[i][j] == 'l':
			#We are inserting a gap in the second sequence
			aln1 = seq1[j-1] + aln1
			aln2 = '-'		 + aln2
			j -= 1	#Move to the left
		else:# T[i][j] == 'u':
			#We are inserting a gap in the first sequence
			aln1 = '-'		 + aln1
			aln2 = seq2[i-1] + aln2
			i -= 1	#Move upper
	
	return {"aln1": aln1, "aln2": aln2, "score": F[-1][-1]}


template = "LLALWGPDPAAAFVNQHLCGSHLVEALYLVCGERGFFYTPKTRREAEDLQVGQVELGGGPGAGSLQPLALEGSLQKRGIVEQCCTSICSLYQLENYCN"
target = "MALWMRLLPLLALLALWGPDPVPAFVNQHLCGSHLVEALYLVCGERGFFYTPKTRREAEDPQVGQVELGGGPGTGSLQPLALEGSLQKRGIVEQCCTSICSLYQLENYCN"


gap = 10


PAM250_dict = {'A': {'A': 2.0, 'R': -2.0, 'N': 0.0, 'D': 0.0, 'C': -2.0, 'Q': 0.0, 'E': 0.0, 'G': 1.0, 'H': -1.0, 'I': -1.0, 'L': -2.0, 'K': -1.0, 'M': -1.0, 'F': -4.0, 'P': 1.0, 'S': 1.0, 'T': 1.0, 'W': -6.0, 'Y': -3.0, 'V': 0.0}, 'R': {'A': -2.0, 'R': 6.0, 'N': 0.0, 'D': -1.0, 'C': -4.0, 'Q': 1.0, 'E': -1.0, 'G': -3.0, 'H': 2.0, 'I': -2.0, 'L': -3.0, 'K': 3.0, 'M': 0.0, 'F': -4.0, 'P': 0.0, 'S': 0.0, 'T': -1.0, 'W': 2.0, 'Y': -4.0, 'V': -2.0}, 'N': {'A': 0.0, 'R': 0.0, 'N': 2.0, 'D': 2.0, 'C': -4.0, 'Q': 1.0, 'E': 1.0, 'G': 0.0, 'H': 2.0, 'I': -2.0, 'L': -3.0, 'K': 1.0, 'M': -2.0, 'F': -4.0, 'P': -1.0, 'S': 1.0, 'T': 0.0, 'W': -4.0, 'Y': -2.0, 'V': -2.0}, 'D': {'A': 0.0, 'R': -1.0, 'N': 2.0, 'D': 4.0, 'C': -5.0, 'Q': 2.0, 'E': 3.0, 'G': 1.0, 'H': 1.0, 'I': -2.0, 'L': -4.0, 'K': 0.0, 'M': -3.0, 'F': -6.0, 'P': -1.0, 'S': 0.0, 'T': 0.0, 'W': -7.0, 'Y': -4.0, 'V': -2.0}, 'C': {'A': -2.0, 'R': -4.0, 'N': -4.0, 'D': -5.0, 'C': 12.0, 'Q': -5.0, 'E': -5.0, 'G': -3.0, 'H': -3.0, 'I': -2.0, 'L': -6.0, 'K': -5.0, 'M': -5.0, 'F': -4.0, 'P': -3.0, 'S': 0.0, 'T': -2.0, 'W': -8.0, 'Y': 0.0, 'V': -2.0}, 'Q': {'A': 0.0, 'R': 1.0, 'N': 1.0, 'D': 2.0, 'C': -5.0, 'Q': 4.0, 'E': 2.0, 'G': -1.0, 'H': 3.0, 'I': -2.0, 'L': -2.0, 'K': 1.0, 'M': -1.0, 'F': -5.0, 'P': 0.0, 'S': -1.0, 'T': -1.0, 'W': -5.0, 'Y': -4.0, 'V': -2.0}, 'E': {'A': 0.0, 'R': -1.0, 'N': 1.0, 'D': 3.0, 'C': -5.0, 'Q': 2.0, 'E': 4.0, 'G': 0.0, 'H': 1.0, 'I': -2.0, 'L': -3.0, 'K': 0.0, 'M': -2.0, 'F': -5.0, 'P': -1.0, 'S': 0.0, 'T': 0.0, 'W': -7.0, 'Y': -4.0, 'V': -2.0}, 'G': {'A': 1.0, 'R': -3.0, 'N': 0.0, 'D': 1.0, 'C': -3.0, 'Q': -1.0, 'E': 0.0, 'G': 5.0, 'H': -2.0, 'I': -3.0, 'L': -4.0, 'K': -2.0, 'M': -3.0, 'F': -5.0, 'P': -1.0, 'S': 1.0, 'T': 0.0, 'W': -7.0, 'Y': -5.0, 'V': -1.0}, 'H': {'A': -1.0, 'R': 2.0, 'N': 2.0, 'D': 1.0, 'C': -3.0, 'Q': 3.0, 'E': 1.0, 'G': -2.0, 'H': 6.0, 'I': -2.0, 'L': -2.0, 'K': 0.0, 'M': -2.0, 'F': -2.0, 'P': 0.0, 'S': -1.0, 'T': -1.0, 'W': -3.0, 'Y': 0.0, 'V': -2.0}, 'I': {'A': -1.0, 'R': -2.0, 'N': -2.0, 'D': -2.0, 'C': -2.0, 'Q': -2.0, 'E': -2.0, 'G': -3.0, 'H': -2.0, 'I': 5.0, 'L': 2.0, 'K': -2.0, 'M': 2.0, 'F': 1.0, 'P': -2.0, 'S': -1.0, 'T': 0.0, 'W': -5.0, 'Y': -1.0, 'V': 4.0}, 'L': {'A': -2.0, 'R': -3.0, 'N': -3.0, 'D': -4.0, 'C': -6.0, 'Q': -2.0, 'E': -3.0, 'G': -4.0, 'H': -2.0, 'I': 2.0, 'L': 6.0, 'K': -3.0, 'M': 4.0, 'F': 2.0, 'P': -3.0, 'S': -3.0, 'T': -2.0, 'W': -2.0, 'Y': -1.0, 'V': 2.0}, 'K': {'A': -1.0, 'R': 3.0, 'N': 1.0, 'D': 0.0, 'C': -5.0, 'Q': 1.0, 'E': 0.0, 'G': -2.0, 'H': 0.0, 'I': -2.0, 'L': -3.0, 'K': 5.0, 'M': 0.0, 'F': -5.0, 'P': -1.0, 'S': 0.0, 'T': 0.0, 'W': -3.0, 'Y': -4.0, 'V': -2.0}, 'M': {'A': -1.0, 'R': 0.0, 'N': -2.0, 'D': -3.0, 'C': -5.0, 'Q': -1.0, 'E': -2.0, 'G': -3.0, 'H': -2.0, 'I': 2.0, 'L': 4.0, 'K': 0.0, 'M': 6.0, 'F': 0.0, 'P': -2.0, 'S': -2.0, 'T': -1.0, 'W': -4.0, 'Y': -2.0, 'V': 2.0}, 'F': {'A': -4.0, 'R': -4.0, 'N': -4.0, 'D': -6.0, 'C': -4.0, 'Q': -5.0, 'E': -5.0, 'G': -5.0, 'H': -2.0, 'I': 1.0, 'L': 2.0, 'K': -5.0, 'M': 0.0, 'F': 9.0, 'P': -5.0, 'S': -3.0, 'T': -3.0, 'W': 0.0, 'Y': 7.0, 'V': -1.0}, 'P': {'A': 1.0, 'R': 0.0, 'N': -1.0, 'D': -1.0, 'C': -3.0, 'Q': 0.0, 'E': -1.0, 'G': -1.0, 'H': 0.0, 'I': -2.0, 'L': -3.0, 'K': -1.0, 'M': -2.0, 'F': -5.0, 'P': 6.0, 'S': 1.0, 'T': 0.0, 'W': -6.0, 'Y': -5.0, 'V': -1.0}, 'S': {'A': 1.0, 'R': 0.0, 'N': 1.0, 'D': 0.0, 'C': 0.0, 'Q': -1.0, 'E': 0.0, 'G': 1.0, 'H': -1.0, 'I': -1.0, 'L': -3.0, 'K': 0.0, 'M': -2.0, 'F': -3.0, 'P': 1.0, 'S': 2.0, 'T': 1.0, 'W': -2.0, 'Y': -3.0, 'V': -1.0}, 'T': {'A': 1.0, 'R': -1.0, 'N': 0.0, 'D': 0.0, 'C': -2.0, 'Q': -1.0, 'E': 0.0, 'G': 0.0, 'H': -1.0, 'I': 0.0, 'L': -2.0, 'K': 0.0, 'M': -1.0, 'F': -3.0, 'P': 0.0, 'S': 1.0, 'T': 3.0, 'W': -5.0, 'Y': -3.0, 'V': 0.0}, 'W': {'A': -6.0, 'R': 2.0, 'N': -4.0, 'D': -7.0, 'C': -8.0, 'Q': -5.0, 'E': -7.0, 'G': -7.0, 'H': -3.0, 'I': -5.0, 'L': -2.0, 'K': -3.0, 'M': -4.0, 'F': 0.0, 'P': -6.0, 'S': -2.0, 'T': -5.0, 'W': 17.0, 'Y': 0.0, 'V': -6.0}, 'Y': {'A': -3.0, 'R': -4.0, 'N': -2.0, 'D': -4.0, 'C': 0.0, 'Q': -4.0, 'E': -4.0, 'G': -5.0, 'H': 0.0, 'I': -1.0, 'L': -1.0, 'K': -4.0, 'M': -2.0, 'F': 7.0, 'P': -5.0, 'S': -3.0, 'T': -3.0, 'W': 0.0, 'Y': 10.0, 'V': -2.0}, 'V': {'A': 0.0, 'R': -2.0, 'N': -2.0, 'D': -2.0, 'C': -2.0, 'Q': -2.0, 'E': -2.0, 'G': -1.0, 'H': -2.0, 'I': 4.0, 'L': 2.0, 'K': -2.0, 'M': 2.0, 'F': -1.0, 'P': -1.0, 'S': -1.0, 'T': 0.0, 'W': -6.0, 'Y': -2.0, 'V': 4.0}}

