#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Patient():
    
    def __init__(self, pName, isInsured, coveragePercent = 0):
        self.__pName = pName
        self.__isInsured = isInsured
        self.set_coveragePercent(coveragePercent)
        self.__hospitalFee = 200
        
        
    def get_pName(self):
        return self.__pName 
    def get_isInsured(self):
        return self.__isInsured
    def get_coveragePercent(self):
        return self.__coveragePercent
    def get_hospitalFee(self):
        return self.__hospitalFee
        
    def set_pName(self, npName):
        self.__pName = npName
    def set_isInsured(self, nisInsured):
        self.__isInsured = nisInsured
    def set_coveragePercent(self, ncoveragePercent):
        if int(ncoveragePercent) >= 0:
            self.__coveragePercent = int(ncoveragePercent)/100   #Turning coverage to a decimal
            
    def __repr__(self):
        if bool(self.get_isInsured()):
            print("Patient Name: " + str(self.get_pName()) + " Insurance: (yes)")
        else: print("Patient Name: " + str(self.get_pName()) + " Insurance: (no)")
        return " "
        
        
    def calculateFee(self):
        return self.get_hospitalFee() * (1 - self.get_coveragePercent())
    
"""
Calculates the hospital fee of the patient.    
    
Parameters:
self

Returns:
(float): Calculated hospital fee of the patient.

"""
        
        
        

