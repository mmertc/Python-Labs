#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def isAllLetter(st):
    for i in st:
        if i.isalnum():              #Checks if alphanumeric.
            for j in "0123456789":   #Checks if number.
                if i == j:
                    return False     #Returns false, if one of them is true.
        else: return False
    return True
    

"""
Checks if the given string consists of only letters.

Parameters:
st (string): string input

Returns:
none
"""   
    
    
def pluralizeWord(st):
    if st[len(st)-1:len(st)] == "y":      #Checks if last char is "y".
        st = st[0:len(st)-1]                     #If so deletes it.
        st = st + "ies"                          #And adds "ies".
        return st
    else: return st + "s"
    
"""
Pluralizes the given word. If it ends with y, drops it and adds "ies". Otherwise just adds "s".

Parameters:
st (string): string input

Returns:
string: Pluralized word
"""   



def pluralizeAllWords(inFName, outFName):
    outOC = 0
    outTC = 0
    inF = open(inFName + ".txt", "r")
    outF = open(outFName + ".txt", "a")
    
    for i in inF:
        if i[len(i)-1:len(i)] == "\n":              #Checks if last char of the line is "\n".
            i = i[0:len(i)-1]                           #If so, deletes it.
        outTC += 1                                  #Counts the total words in the input file.
        if isAllLetter(i):      
            outF.write(pluralizeWord(i) + "\n")     #If all letter, adds to the output file.
            outOC += 1                              #Counts the added words.
    outF.write(str(round((outOC/outTC)*100, 2)) + "% of the words are pluralized") #Types the pluralized percentage into the file
    inF.close()
    outF.close()
    
    
    
    
    
"""
For every word in the input file, checks if it only consists of lettes. If so, pluralizes it and then appends it to the output file. Also adds the pluralized percentage at the end.

Parameters:
inFName (string): Input file's name
outFName (string): Output file's name

Returns:
none
"""  

