#!/usr/bin/env python
# coding: utf-8

# In[1]:


def sumDigits(n):
    ssum = 0    
    for i in range(1, n+1):
        while i >= 1:     #Continues to extract the last digit until it hits 0.
            tsum = i % 10 #Gets the last digit of the number.
            i -= tsum     #Omits the last digit 1/2.
            i /= 10       #Omits the last digit 2/2.
            ssum += tsum  #Adds the taken digit to the main sum.
    return int(ssum)

"""
Takes the sum of all the integers' digits from 0 to n (inclusive).

Parameters:
n (int): Integer input

Returns:
int: ssum
"""

num = int(input("Enter a positive integer: "))
if num <= 0: print("Value must be Positive!") 
else: print("The sum of the digits in the number from 1 to " + str(num) + " is " + str(sumDigits(num)))


# In[ ]:




