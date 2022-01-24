#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import doctor as dr


def read_doctors(txtN):
    txt = open(txtN + ".txt", "r")
    L = txt.readlines()
    oL = []   #An empty list for the Doctor objects
    
    
    for i in range(0, len(L)):    #Splits the lines of the txt and initiates Doctor objects with them. And appends them to the oL.
        L[i] = L[i].split(";")
        oL.append(dr.Doctor(L[i][0], L[i][1], L[i][2], L[i][3]))
        
    return oL  #The list of Doctor objects.

"""
Creates a list of Doctor objects initiated with the info from the given txt.

Parameters:
txtN (str): Name of the txt file.

Returns:
oL (list): Created doctor list.

"""

def bubble_sort(oL):
    done = False  #Ending criteria for the sorter.
    
    while (not done): #Sorter
        done = True  #Initially true, if doesn't turn to false during an iteration, loop will terminate.
        for i in range(1,len(oL)):    
            if oL[i-1].get_hospital() <= oL[i].get_hospital():   #If the current two objects order is correct, passes them.                            
                if oL[i-1].get_hospital() == oL[i].get_hospital():
                    if oL[i-1].get_specialty() <= oL[i].get_specialty():
                        continue
                else: continue
                          
            temp = oL[i]       #If not, corrects.
            oL[i] = oL[i-1]
            oL[i-1] = temp
            done = False     #If needs to correct anywhere during the run, makes it need another go. So a perfect run terminates the iterations.
 
"""
Sorts the given doctors list alphabetically according to their hospital name and specialty.

Parameters:
oL (list): List to sort.

Returns:
none

"""

def binary_search(L, seID, stID, enID): 
    if(stID > enID):   #Checks if couldn't found.
        return -1
    else:
        mid = (stID + enID)//2    #Gets the midpoint, rounds below if not int.
        if(L[mid].get_doctor_id() == seID):         #Checks if the searching value is the mid point.
             return mid             #If yes, returns the index.
        
        elif(L[mid].get_doctor_id() > seID):        #If it is past/before the mid, recalls itself with the new boundaries.
            return binary_search(L, seID, stID, mid-1)
        else:
            return binary_search(L, seID, mid+1, enID)
    
"""
Binary searches for the given ID within the given list. 

Parameters:
L (list): List to search within.
seID (int): ID to search
stID (int): Lower boundary for the binary search.
enID (int): Upper boundary for the binary search.

Returns:
mid (int): Index of the doctor with the given ID.
-1: If no such doctor exists. 

"""       



dL = read_doctors("doctors")   #Gets the doctor list.


done = False  #Ending criteria for the sorter. 
while (not done): #Sorter
    done = True  #Initially true, if doesn't turn to false during an iteration, loop will terminate.
    for i in range(1,len(dL)):          
        if dL[i-1] < dL[i]:   #If the current two objects order is correct, passes them.
            continue
                
        temp = dL[i]       #If not, corrects.
        dL[i] = dL[i-1]
        dL[i-1] = temp
        done = False      #If needs to correct anywhere during the run, makes it need another go. So a perfect run terminates the iterations.

seID = input("Enter id of doctor to search: ")

index = binary_search(dL, seID, 0, len(dL))  #Finds the index of the doctor with the desired ID.
if index != -1:   #Prints it.
    print("Doctor with id " + str(seID))
    print(dL[index])
else: print("No such doctor")
    
print("--------------------------------")
print("Doctors by Hospital and Specialty: ")    

bubble_sort(dL) #Sorts the doctors alphabetically.
print()
for i in dL:  #And prints the alphabetically sorted list of the doctors.
    print(i)


# In[ ]:




