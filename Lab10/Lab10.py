#!/usr/bin/env python
# coding: utf-8

# In[157]:


import matplotlib.pyplot as plt
import numpy as np

np.set_printoptions(suppress=True)

countries = np.loadtxt("countries.txt", skiprows=1, dtype="str")  #Loading the arrays from the txts.
indicators = np.loadtxt("indicators.txt", skiprows=1)

a = indicators[:, 6:7] < 1000
indicators_under_1000 = indicators[a.reshape(len(a))]    #Getting only the rows with <1000GDP.

b = countries[:, 1:].reshape(len(countries)) == "Europe" 
europe_countries = countries[b]  #Getting only the Europe rows
europe_data = indicators[b]     #And their indicatos


c = countries[:, :1].reshape(len(countries)) == "Turkey"
trIndex = np.where(c)  #Turkey's index in this particular txt

turkey_employment_data = indicators[trIndex, 7:9].reshape(2)   #Creating an employment data array for Turkey.


plt.figure(0)
plt.subplot(1, 2, 1)
plt.title("Life Expectancy for Europe by Gender")  #Customising the graph.
plt.ylabel("Life Expectancy")
plt.xticks([0 ,1], ["Europe Male", "Europe Female"])
plt.legend(["Men", "Women"])

lifeExEu = np.array([np.mean(europe_data[:, 3:4]), np.mean(europe_data[:, 4:5])])  #Calculating the mean life exp. of europe

plt.bar([0], lifeExEu[0])   #Creating the graphs.
plt.bar([1], lifeExEu[1])


plt.subplot(1, 2, 2)


plt.title("Infant Mortality with GDP under 1000") #Customising the graph.
plt.xlabel("GDP")
plt.ylabel("Infant Mortality")
plt.plot(indicators_under_1000[:, 6:7].reshape(len(indicators_under_1000)), indicators_under_1000[:, 5:6].reshape(len(indicators_under_1000)) , "*--")


plt.figure(1)  #Opening another figure window.
plt.subplot(2, 1, 1)

plt.pie(turkey_employment_data, autopct="%1.1f%%", explode=[0, 0.1], labels=["Male", "Female"])
plt.title("Employment Rates by Gender in Turkey")


ob = plt.subplot(2, 1, 2)
edges = plt.hist(indicators[:, :1].reshape(len(indicators)), 4)
plt.title("Frequency of Fertility Rates for All Countries (4 bins)")
ob.set_xticks(edges[1])   #Setting the edges of bins to the precise values.

