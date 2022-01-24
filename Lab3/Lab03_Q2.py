#!/usr/bin/env python
# coding: utf-8

# In[1]:


def hailstone(num):
    print(num, end=" ") #Prints the current input num
    if num == 1:   #Ends the incursion if num hits 1
        print("")
        return    
    if (num % 2) == 0:  
        num /= 2   
    else: num = (3*num + 1)
    hailstone(int(num))   #After doing required operations, it passes the num to next iteration of the incursion. 
    
""""
Calcutes and prints the hailstone sequence of the given number.

Parameters:
num (int): integer input

Returns:
none

"""

hailstone(5)
hailstone(6)
hailstone(7)
hailstone(8)
hailstone(9)
hailstone(10)


# In[ ]:




