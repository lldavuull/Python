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
def worst_case(data):
    file=open(data,'r')                   #Timing Analysis of the CAN Protocol
    message_number=int(file.readline())          #number of messages.
    tau=float(file.readline())                   #Minimum value
    strlines=file.readlines()                    #all string lines
    pct=[]
    for str in strlines:
        pct.append(str.split())                  #priority(Pi), transmission time(Ci), period of each message(Ti).
    pct=np.array(pct)
    pct = pct.astype(np.float64)
#    print(pct[3:,0],)
    for i in range(message_number):
        #Qi=Bi+sum{[(Qi+tau)/Tj]*Cj}
              #j, Pj<Pi
        Bi=max(pct[i:,1])    #Q=B in first step
        if i==0:            #priority==0, skip next
            print("perioid ",i," worst-case response time: ", Bi+pct[i,1])
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
        print("perioid ",i," worst-case response time: ", Qi+pct[i,1])
    file.close()
worst_case('Input.dat')