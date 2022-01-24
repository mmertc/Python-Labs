#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import Stock as st

tmP = open("input.txt", "r")
cL = tmP.readline()
oL = []                             #List to store the objects.

while cL != "":                                             #Reads the lines one by one until the end of the txt file.
        cLL = cL.split(";")
        oL.append(st.Stock(cLL[0], cLL[1], cLL[2], cLL[3])) #Creates an object with the info from the current line and adds to the list.
        cL = tmP.readline()
        
        
def getByStockQuantity(oL, n):
    rL = []
    for i in oL:
        if int(i.get_count()) > n:         #Checks if stock count is larger than the provided value.
            rL.append(i)                   #If so, appends to the list to return at the end.   
    return rL


"""
Finds the stock items with more than "n" in stock and return them as a list.

Parameters:
oL (list): List of objects to look into.
n (int): Stock quantity to compare to.

Returns:
rL (list): List of objects that is compatible with the condition.
"""


def getByPrice(oL, lPrice):
    rL = []
    for i in oL:
        if float(i.get_price()) < float(lPrice):        #Checks if price is smaller than the provided value.
            rL.append(i)                                #If so, appends to the list to return at the end.
    return rL
    
    
    
"""
Finds the stock items which are cheaper than "lPrice" and return them as a list.

Parameters:
oL (list): List of objects to look into.
lPrice (float): Price to compare to.

Returns:
rL (list): List of objects that is compatible with the condition.
"""
    
    
a = getByStockQuantity(oL, 6)            #Gets the ones with more than 6 in stock.
b = getByPrice(oL, 5)                    #Gets the ones that are cheaper than 5.

for i in a:
    for j in b:
        if i == j:                       #Finds the objects that appear in both of the lists a, b.
            print(i)                     #Ands prints it.
            b.remove(j)         #No need to look for the current object in the future as it is already found, thus deleted for optimisation.
            break               #No need to search in rest of the list as it is already found.
    



    

