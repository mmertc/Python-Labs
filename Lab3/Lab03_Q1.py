#!/usr/bin/env python
# coding: utf-8

# In[ ]:


vowels = "aeoui"

def is_vowel(st):
    if len(st) == 1:   #Checks if it is just one character.
        for i in vowels:  #Checks if it is a vowel.
            if st == i:                
                return True
    return False

"""
Checks if the given string is a single character vowel. 

Parameters:
st (string): Input string

Returns:
bool
"""

def count_vowels(st):
    c = 0
    for i in st:
        if is_vowel(i):   #If current char is a vowel, it increases c by one.
            c += 1
            
    return c
            
"""
Counts the number of vowels in the given string. 

Parameters:
st (string): Input string

Returns:
int: c
"""

def all_vowels(st):
    tvowels = "aeoui"  #A dummy variable that contains all the vowels.
    for i in st:
        for j in vowels:
            if i == j:    #For every vowel in the st, it deletes it from the tvowels.        
                tvowels = tvowels.replace(j, "")  
    if tvowels == "": return True  #So at the end if there's no more undeleted char in the tvowels, all vowels exist.
    else: return False
    
"""
Checks if the given string contains all the vowels. 

Parameters:
st (string): Input string

Returns:
bool
"""

def display_which_vowels(st):
    sa = False
    se = False
    si = False   #Just to make sure it gets printed only one time.
    so = False
    su = False
    for i in st:
        if i == "a" and sa == False:  
            print("'a' exists in " + st)
            sa = True   #Makes it true so no more prints for that vowels.
        elif i == "e" and se == False:
            print("'e' exists in " + st)
            se = True
        elif i == "i" and si == False:
            print("'i' exists in " + st)
            si = True
        elif i == "o" and so == False:
            print("'o' exists in " + st)
            so = True
        elif i == "u" and su == False:
            print("'u' exists in " + st)
            su = True
                
"""
Prints that if a vowel exits in the given string.

Parameters:
st (string): Input string

Returns:
none
"""

def capitalize_vowels(st):
    for i in st:
        if is_vowel(i):  
            st = st.replace(i, i.upper())  #If the current char is a vowel, it capitalizes the vowel.
    return st
        
"""
Capitalizes the given vowel.

Parameters:
st (string): Input vowel.

Returns:
string: st

"""
    
    
s = input("Enter a string: ")
print("There are "+ str(count_vowels(s)) + " number of vowels")
if all_vowels(s): print("All Vowels exist in the given string.") 
display_which_vowels(s)
print("New String: " + capitalize_vowels(s))
input()
        
    


# In[ ]:




