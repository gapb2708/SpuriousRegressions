#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
plt.rcParams["figure.figsize"] = (15, 25)  #set default figure size
from statistics import mean

def sim(a,b,sim_lenght,time):

    t_lenght=np.linspace(0, time, num=time)

    ϵ=np.zeros((len(t_lenght),sim_lenght))
    for t in range (0,sim_lenght):
        ϵ[:,t]=np.random.randn(len(t_lenght))
    y=np.zeros((len(t_lenght),sim_lenght//2))
    for t in range (0,sim_lenght//2):
        for s in range(0,len(t_lenght)):
            if s==0:
                y[0,:]=1/(1-b)
            else:
                y[s,t]=a+b*y[s-1,t]+ϵ[s,t]  
    x=np.zeros((len(t_lenght),sim_lenght//2))
    for t in range (0,sim_lenght//2):
        for s in range(0,len(t_lenght)):
            if s==0:
                x[0,:]=1/(1-b)
            else:
                x[s,t]=a+b*x[s-1,t]+ϵ[s,t+10]

    fig, axs = plt.subplots(sim_lenght//4+1,2)
    fig.subplots_adjust(hspace = 0.08, wspace=.05)
    axs = axs.ravel()

    for i in range(sim_lenght//2):
        axs[i].plot(t_lenght,(y[:,i]))
        axs[i].plot(t_lenght,(x[:,i]))
    reg=[]
    avg_p=[]
    for i in range (sim_lenght//2):
        X=x[100:,i]
        X=sm.add_constant(x[100:,i])
        Y=y[100:,i]
        reg.append(sm.OLS(Y, X).fit())
        avg_p.append(((reg[i].pvalues[1]<0.05)))
    return print("la proporcion de coeficientes significativos es de: " +str(round(avg_p.count(True)/(sim_lenght/2),2))+"%")
    
sim(1,0.55,50,600)

