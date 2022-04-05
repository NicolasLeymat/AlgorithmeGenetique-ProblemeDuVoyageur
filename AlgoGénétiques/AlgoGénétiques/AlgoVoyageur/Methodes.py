# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 10:20:59 2021

@author: leyma
"""
import random as r

#Verirfie si i est contenu dans le tableau/list
def contains(lst, i) : 
    if lst.count(lst[i]) > 1 : 
        return True
    else :
        return False

#verifie quelle tableau est le plus grand
def plusGrandeLen(t1,t2) : 
    if len(t1) > len(t2) :
        return len(t1)
    elif len(t2) > len(t1) : 
        return len(t2)
    else :
        return len(t1)
    
#Calcule le nombre de vills qui sont en plus de 1 fois dans le tableau
def villesDupliquer(t,nbMaxDeVilles) : 
    x = 0
    for i in range(0,len(t)) : 
        if t.count(i)>1 :
            x += 1
        i+=1
    return x


def villesDupliquerIndex(t,nbMaxDeVilles) : 
    for i in range(0,len(t)) : 
        if t.count(i)>1 :
            return i
        i+=1

        
def villesUniques(t1,t2) :
    x = 0
    t = []
    for x in range(0,plusGrandeLen(t1, t2)):
        t.append(t1[x])
        t.append(t2[x])
        x+=1
    
    for y in range(0,len(t)) : 
        if contains(t, y) == False : 
            return t[y]
        y+= 1
   
        

def index(val, t1):
    for i in range(0,len(t1)):
        if(val == t1[i]):
            return i
    
