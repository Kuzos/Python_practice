
def create_matrices(seq1,seq2,matrix,gap):

    score_matrix=[]   #creating scoring matrix
    backT_matrix=[]   # creating backtrack matrix

    for row in range(len(seq2)+1):
        score_matrix.append([])             #givving it right demsion on rows(seq2)
        backT_matrix.append([])
        for column in range(len(seq1)+1):
            score_matrix[row].append(0)     # giving right demnsion on columns seq1
            backT_matrix[row].append(" ")
    
    #just checking if everything is okay 
       #lenghts 110,111 it is correct because we have one more 
      # lenghts98,99 it is correct because we have one more

    #intialazing first row and column
    for i in range(1,len(seq2)+1):
        score_matrix[i][0]=i*gap
        backT_matrix[i][0]='u'
        for j in range(1,len(seq1)+1):
            score_matrix[0][j]=j*gap
            backT_matrix[0][j]='l'
    #last one is 980 its okay
     # small concern i need end on 0,0 also because thats how its stoping in imported function 
    backT_matrix[0][0]='end'
   
    #for each in range(1,len(seq2)+1):
        #print(score_matrix[each][0]) #last one is 1100 so its okay
    
    #now all thats left is to fill matrix
    # had an error with extracting values from pam so just checking the structure
    for i in range(1,len(seq2)+1):    #we go from one because first row and column are gaps
        for j in range(1,len(seq1)+1):
            sd=score_matrix[i-1][j-1]+PAM250_dict[seq2[i-1]][seq1[j-1]],'d'  #if match, take score from substition dict and write d in backtrackmatrix
            su=score_matrix[i-1][j] +gap,'u'     #if u its gap in first sequcence, thats why j is unchanged, we put u in backtrackmatrix
            sl=score_matrix[i][j-1] +gap,'l'     #if l its gap in secound sequence , thats why i is unchanged, we put l in backtrackmatrix 
            score_matrix[i][j],backT_matrix[i][j]=max(sd,su,sl) #taking the max based on score, take in mind each score is tupple with contains score and string for backtrack matrix
    return score_matrix,backT_matrix


if __name__=="__main__":
    from input_data import *
    seq1=template  #remember you use j for seq1, this one is on colums it goes secound [i][j]
    seq2=target   #remember you use i for seq2, this one is on the rows it goes first [i][j]
    F,T=create_matrices(seq1,seq2,PAM250_dict,-gap)
    Final=backtrack(seq1,seq2,F,T)  #calling imported function with F,T matrices as asked(F is scoring one),T(is traceback matrix)
    print("This is align from first sequence",Final['aln1'])  #coulda done loop also but this is okay we only have 3 keys
    print("This is align from secound sequence",Final['aln2'])
    print("This is the score of the alignment",Final['score'])
    
    

