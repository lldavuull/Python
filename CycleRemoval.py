# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 17:50:55 2019
@author: AzuMeow

Input1.dat
1024   vertex
1027   edges
  39  105
  71  202
 104  299
 136  396
 168  493
 201  590
 233  687
 265  784
 298  881
 330  978
  20   48
  52  145
  85  242
 117  339
 149  436
 182  533
 214  630
 246  727
 279  824
 311  921
 343 1018
dfs
"""

#use dfs    
class graph():
    def __init__(self,input):
        self.input=input
        self.graph={}
        self.newRoot=False
        file=open(input,'r')                   
        self.vertexNumber=int(file.readline())+1  
        edgeNumber=int(file.readline())                 
        strlines=file.readlines()                    
        file.close()
        firstFilled=[True]*self.vertexNumber
        for str in strlines:
            vertex=list(map(int,str.split()))
            if firstFilled[vertex[0]]:
                firstFilled[vertex[0]]=False
                self.graph[vertex[0]]=[vertex[1]]
            else:
                self.graph[vertex[0]].append(vertex[1])
    def detectCycle(self):
        self.Cycle=False
        print('Detect whether',self.input,'has Cycle.')
        for source in self.graph:
            self.root=source
            self.discover(source)
            self.newRoot=False
        if not self.Cycle:
            print(self.input,'No Cycle!')
    def discover(self,source):
        if source not in self.graph:
            return
        targets=self.graph[source].copy()
        for target in targets:
            if self.newRoot:
                self.newRoot=False
                self.root=source
            if self.root==target:
                print("remove:",source,target)
                self.graph[source].remove(target)
                self.Cycle=True
                
                if self.graph[source]:
                    self.root=source
                    self.newRoot=False
                else:
                    self.newRoot=True
            else:
                self.discover(target)
graph1=graph('Input1.dat')
graph1.detectCycle()
graph2=graph('Input2.dat')
graph2.detectCycle()