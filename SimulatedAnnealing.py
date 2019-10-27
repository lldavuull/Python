# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 17:50:55 2019
@author: AzuMeow

Input.dat
17
0.002
 0 0.52 50
 1 0.60 5
 2 0.52 5
 3 0.60 5
 4 0.52 5
 5 0.60 5
 6 0.92 10
 7 0.52 10
 8 0.60 10
 9 0.68 10
10 0.52 50
11 0.76 100
12 0.52 100
13 0.52 100
14 0.68 1000
15 0.52 1000
16 0.52 1000
"""
import numpy as np
import math

def worst_case_cost(message_number,tau,pct):
#    print(pct[3:,0],)
    worst_response_time=0
    for i in range(message_number):
        #Qi=Bi+sum{[(Qi+tau)/Tj]*Cj}
              #j, Pj<Pi
        Bi=max(pct[i:,1])    #Q=B in first step
        if i==0:            #priority==0, skip next
            continue
        Qi=Bi               #left=Bi
        while True:         #emulate do-while
            right=Bi
            for j in pct[:i]:       #j=[0~i)
                right=right+math.ceil((Qi+tau)/j[2])*j[1]
#            if i==1:
#                print("period ",i,", ",j[0],": ",right," Qi:",Qi)
            if Qi==right:
                break
            else:
                Qi=right
        worst_response_time=Qi+pct[i,1]+worst_response_time
    return worst_response_time

def neighborState(current,message_number):
    swap1=np.random.randint(message_number)
    swap2=np.mod(swap1+np.random.randint(1,message_number),message_number)
    neighbor=current
    neighbor[[swap1,swap2],:]=neighbor[[swap2,swap1],:]
    return neighbor
    
def find_good_priority(data):
    file=open(data,'r')                   #Timing Analysis of the CAN Protocol
    message_number=int(file.readline())          #number of messages.
    tau=float(file.readline())                   #Minimum value
    strlines=file.readlines()                    #all string lines
    file.close()
    pct=[]
    for str in strlines:
        pct.append(str.split())          #priority(Pi), transmission time(Ci), period of each message(Ti).
    pct=np.array(pct)
    pct = pct.astype(np.float64)
    
    best_time=worst_case_cost(message_number,tau,pct)
    
    episode=0
    print("episode",episode,":",best_time)
    T=10000      #Temprature
    coolingFactor=0.9998
    current=pct
    current_time=best_time
    while(T>10):
        episode=episode+1
        neighbor=neighborState(current,message_number)
        neighbor_time=worst_case_cost(message_number,tau,neighbor)
        delta=neighbor_time-current_time
        if delta < 0:
            current_time=neighbor_time
            current=neighbor
            if best_time>current_time:
                pct=current
                best_time=current_time
                print("episode",episode,":", best_time)
        elif np.random.rand()<np.exp(-delta/T):
            current_time=neighbor_time
            current=neighbor
        T=T*coolingFactor
    print(pct[:,0])
    
find_good_priority('Input.dat')