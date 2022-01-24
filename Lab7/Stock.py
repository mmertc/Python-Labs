#!/usr/bin/env python
# coding: utf-8

# In[17]:


class Stock:
    def __init__(self, name, count, price, city):  #Initiating the variables of the class.
        self.__name = name
        self.__count = count
        self.__price = price
        self.__city = city
        
    def __repr__(self):                            #Creating the procedure for print(object).
        print("Name: " + str(self.__name))
        print("Count: " + str(self.__count))
        print("Price: " + str(self.__price))
        print("City: " + str(self.__city))
        return ""
    
    def get_name(self):                            #Creating get/set functions.
        return self.__name
    def get_count(self):
        return self.__count
    def get_price(self):
        return self.__price
    def get_city(self):
        return self.__city
        
    def set_price(self, nprice):
        self.price = nprice
        
        
"""
Get/Set functions to interact with the private variables from outside of the class.

"""

