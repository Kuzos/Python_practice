


file1=open("input.txt",'r')
file2=open("dict.txt",'r')
file3=open('output.txt','a')   
""" Reading all necessary files """
ls_dict=[]            #creating list for corrected words

for word in file2:       #looping through dict.txt and appending each word
    word=word.rstrip()
    ls_dict.append(word)
#print(ls_dict)          #checking that list contains everything

def correct_word(some_word,ls_dict):
    """This is function for checking if word is correct, if the word is in ls_dict it returns true
    if word is correct but not in dict it returns correct and if its not it returns false"""
    if word in ls_dict:
        spelled=True           #checking if its in ls_dict
        return True
    else:
        answer=input("If word:" + " "+ str(some_word)+ " "+"is correct,type yes, if not type no")
        if answer=="yes":    #checking if user determines that it should be in the dict"
            return "correct"
        else:
            return False
        #word is incorrect

for word in file1:
    word=word.rstrip()
    func=correct_word(word,ls_dict)
    if func==True:
        file3.write("\n" +word)
    elif func=='correct':
        file3.write("\n" +word)
        ls_dict.append(word)
    else:
        spelled=False
        while spelled==False:
            correct_version=input("Please enter correct version of the word")
            c=correct_word(correct_version,ls_dict)
            if c==True:
                file3.write('\n' +correct_version)
                
                spelled=True
            elif c=='correct':
                file3.write( '\n' +correct_version )
                ls_dict.append(correct_version)
                spelled=True
            else: continue
file4=open('output.txt','r')

print(ls_dict)
for line in file4:
    print(line)



