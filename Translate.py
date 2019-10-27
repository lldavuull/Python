# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 13:54:15 2018

@author: root_2
"""

oldFile=open('old_zhTW.txt','r', encoding = 'utf8')
newFile=open('new_enUS.txt','r', encoding = 'utf8')
translateFile=open('translate_zhTW.txt','w',encoding = 'utf8')

olddict={}

for oF in oldFile:
    oFlist=oF.split('=')
    olddict.update({oFlist[0]:oF})


for nF in newFile:
    nFlist=nF.split('=')
    if nFlist[0] in olddict:
        translateFile.write(olddict[nFlist[0]])
    else:
        translateFile.write(nF)