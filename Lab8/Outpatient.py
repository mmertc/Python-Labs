#!/usr/bin/env python
# coding: utf-8

# In[32]:


import Patient as p
import datetime

class Outpatient(p.Patient):
    
    def __init__(self, name, date, time, dName, pClinic, ins, coverage = 0):
        if pClinic == "Dentistry" or pClinic == "Optometry": #If policlinic is one of these, coverage is halved.
            coverage = int(coverage)/2
            
        super().__init__(name, ins, coverage)
        self.__appointmentTime = time
        self.__doctorName = dName
        self.__polyClinic = pClinic
        self.set_appointmentDate(date)
        
        
    def set_appointmentDate(self, date):
        self.__appointmentDate = datetime.datetime.strptime(date, '%Y%m%d').date() #Saving it as a date object.
        
    def __repr__(self):
        print("Appointment Date: " + str(self.__appointmentDate) + " " + str(self.__appointmentTime))
        super().__repr__()
        print("Poly Clinic: " + self.__polyClinic + " (" + self.__doctorName + ")")
        print("Fee: " + str(round(self.calculateFee(),2)))
        return ""
    
    
    def __lt__(self, other):  #Overriding the __lt__ method to compare the times of appointment.
        if self.__appointmentDate == other.__appointmentDate:  #Inside here is for comparing the times of appointment in case dates are same. Works by comparing the time's parts in correct priority.
            if self.__appointmentTime[:2] == other.__appointmentTime[:2]:
                if int(self.__appointmentTime[3:]) < int(other.__appointmentTime[3:]): return True
                else: return False
            elif int(self.__appointmentTime[:2]) < int(other.__appointmentTime[:2]): return True
            else: return False
        elif self.__appointmentDate < other.__appointmentDate: return True
        else: return False

