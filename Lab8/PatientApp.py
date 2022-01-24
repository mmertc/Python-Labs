#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import Outpatient as op



def schedulePatients(txtName):
    mpR = open(txtName + ".txt", "r")
    oL = [] #An empty list for the objects.

    for i in mpR.readlines():
        ii = i.split(";")
        if len(ii) == 6:  #Checks if current patient has insurance, as having it makes the line have 6 elements.
            oL.append(op.Outpatient(ii[0], ii[1], ii[2], ii[3], ii[4], ii[5]))
        else: oL.append(op.Outpatient(ii[0], ii[1], ii[2], ii[3], ii[4], ii[5], ii[6]))  #Initiates the objects and adds them to the list.
   

    done = False  #Ending criteria for the sorter.
    
    while (not done): #Sorter
        done = True  #Initially true, if doesn't turn to false during an iteration, loop will terminate.
        for i in range(1,len(oL)):          
            if oL[i-1] < oL[i]:   #If the current two objects order is correct, passes them.
                continue
                
            temp = oL[i]       #If not, corrects.
            oL[i] = oL[i-1]
            oL[i-1] = temp
            done = False      #If needs to correct anywhere during the run, makes it need another go. So a perfect run terminates the iterations.
            
            
    for i in oL:  #Prints the now sorted contents.
        print(i)
                
        
"""
Takes the name of a txt and turns its contents into a sorted outpatient objects list. And prints them.

Parameters:
txtName (string): The name of the txt file.

Returns:
none
"""
    
schedulePatients("patients")


# In[ ]:




