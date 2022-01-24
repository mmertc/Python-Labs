#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math

def estimateE(n):
    global eT
    eT = tuple(("+1",))    #Initiates the tuple with the first element.
    for i in range(1,n+1):
        eT = eT + tuple(("+"+str(1/math.factorial(i)),))  #Calculates and adds the next element to the end of the tuple.
    return eT

"""
Finds the first n+1 elements of the sequence that calculates euler's number. Which is 1 + 1/1! + 1/2! + ... + 1/n!

Parameters:
n (int): Integer input for the n in the formula.

Returns:
tuple: eT
"""
    
n = int(input("Enter the value of n: "))
print("E = " + str(estimateE(n)))
s = 0
for i in eT:
    s += float(i)   #Gets the sum of the values in the tuple.
    
print("Estimated Value: " + str(s))
print("Error = " + str(math.e - s))
input()
    
    

