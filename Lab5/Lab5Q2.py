#!/usr/bin/env python
# coding: utf-8

# In[4]:


def seperate(ls):
    Rdict = dict({})   
    
    for i in ls:
        isAppended = False     #To control if a new list as a value must be created.
        for j in Rdict:
            if j == str(type(i)):  #Checks if this key exists
                Rdict[str(type(i))] += list((i,))  #If it does, just appends it
                isAppended = True   #And prevents from being overwritten
                break
        if isAppended == False: Rdict[str(type(i))] = list((i,))   #If there were no instance of this key already, creates it.
        
    return Rdict

"""
Takes in a list, returns a dictionary of each different type as keys and the list of elements of that type as a value.

Parameters:
ls (list): List input to operate on.

Return:
dictionary: Rdict

"""
         
           
lss = (2, 3.75, False, 'Today', 'CS115', 6, 1.5, 4.0, 'python', True, 25, 1.9)    

print("Original List = " + str(lss))

for i in seperate(lss).items():     #Prints the dict in the desired format.
    print(i[0] + " -> " + str(i[1]))
    
            
        
        
        


# In[ ]:




