#!/usr/bin/env python
# coding: utf-8

# In[10]:


def form(fN):
    words = list(())
    numbers = list(())
    tStr = ""                            #A temp string for char moving purposes.
    ftR = open(fN + ".txt", "r")
    
    fC = ftR.read()
    fC += "\n"                          #Adds \n to the end because the algorithm depends on it to end the line.
    
   
    for i in fC:   
        if not i.isspace():             #If it is a valid char, then adds to the tStr.
            tStr += i
        elif i == " ":                  #When founds a space, moves the contents of the tStr to the adequate list.
            words.append(tStr)
            tStr = ""
            continue
        else:                           #It is a word if the following space is " ", it is a number if the following space is \n.
            numbers.append(tStr)
            tStr = ""
            continue   
            
    tStr = ""                           #Gets emptied because will be used for storing the sentence.
    sN = 1                              #Initiates the searching position number.
    
    while sN != len(numbers):
        for i in range(0, len(numbers)): 
            if numbers[i] == str(sN):           #Because the lists are parallel, algorithm tries to find the next position number in the sentence. 
                tStr += " " + words[i]          #When finds, it adds the corresponding word the the sentence.
                sN += 1                         #Increases searching position number after each successful iteration

    return tStr
    
    
    
"""
Inputs a txt file's name and reads the words and their positions from that file.
And then forms a sentence in ascending order of their position numbers.

Parameters:
fN (string): The of the input txt file.

Returns:
(string): tStr

"""
print(form("words"))

    
    

