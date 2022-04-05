# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 13:17:08 2021

@author: leyma
"""



import numpy as np
import matplotlib.pyplot as plt
import random as rd
import Methodes as m


#Description des fonctions

#Nous créons la prochaine génération et calculons sa fitness
def nextGen(gen, aTab, nTab,tabSorted,dim):
    aTab.append(tabSorted[0][0])
    for w in range(0,int(dim/2),1):
        randomInteger = rd.randint(1,N-1)
        popI = pop_Sorted[w][0]
        popJ = pop_Sorted[w+1][0]
        aTab.append(crossover(popI, popJ, randomInteger))
    
    for i in range(1, len(aTab)):
        aTab[i] = aTab[i].tolist()

    fillChemin(aTab)

    for x in range(0,len(aTab)):
        while m.villesDupliquer(aTab[x], N) > 0:
            aTab[x][m.index(m.villesDupliquerIndex(aTab[x],N),aTab[x])] = m.villesUniques(aTab[0],aTab[x])

    for i in range(0,M,1):
        for j in range(0,N,1):
            chemin[j] = aTab[i][j]
        d = distance()
        tuples = (aTab[i],d)
        nTab.append(tuples)
        #print('Chromosome : ',i,'Génération  : ',gen,' ', aTab[i],' distance = ',d)
    tabSorted = sorted(nTab,key = lambda x: x[1], reverse = False)
    return tabSorted

#Vu que les enfants sont divisée par 2 il nous manque des individus donc nous remplissons notre tableau avec cette fonction
def fillChemin(tab):
    for i in range(len(tab),M,1):
        tab.append([0]*N)
        for j in range(0,N,1):
            bool = 1
            if j == 0 : 
                element = rd.randint(0, N-1)
            else : 
                while bool == 1:
                    element = rd.randint(0, N-1)
                    l = 0
                    for k in range(0,j,1):
                        if tab[i][k] == element:
                            bool=1
                            l+=l+1
                        if l == 0:
                            bool = 0
            tab[i][j] = element
    return tab

#nous dit si la mutation à lieu
def mutate(pourcentageDeMutation, dim,x):
    if x < pourcentageDeMutation:
        return True
    elif x > pourcentageDeMutation : 
        return False
    elif dim > 100 or dim < 0 : 
        return plt.errorbar

#effectue la mutation
def mutation(mutates, tab, nbRand,i):
    if mutates == True:
        
        tab[i][1]*nbRand
        
        return tab[i][1]
    else:
        return tab[i][1]

#Créer la générations 0/Initial
def creation(tab, Dimension, tabEnfants):
    for i in range(0,M,1):
        tab.append([0]*N)
        for j in range(0,N,1):
            bool = 1
            if j == 0 : 
                element = rd.randint(0, N-1)
            else : 
                while bool == 1:
                    element = rd.randint(0, N-1)
                    l = 0
                    for k in range(0,j,1):
                        if tab[i][k] == element:
                            bool=1
                            l+=l+1
                        if l == 0:
                            bool = 0
            tab[i][j] = element
            chemin[j] = tab[i][j]
        d = distance()
        tuples = (tab[i],d)
        tabEnfants.append(tuples)
        #print('Chromosome',i,' ', tab[i],' distance = ',d)
        plt.plot(x[chemin],y[chemin], color='w')

#calcul la fitness(ici la distance)  
def distance():
    global chemin
    distance = 0.0
    xy = np.column_stack((x[chemin],y[chemin]))
    distance = np.sum(np.sqrt(np.sum(xy - np.roll(xy,-1,axis = 0),axis = 1)**2 ))
    return distance

#fait un crossover des 2 tableau en parametre en fonction d'un nombre x random
def crossover(t1,t2,x):
    tNew = np.append(t1[:x],t2[x:])
    return tNew


N = int(input("Entrez le nombre de ville : "))  # Nb de ville
M = int(input("Entrez le nombre d'individus: "))  # dimension de la population
k = 0  # Compteur de la boucle
genMax = int(input("Entrez le nombre de générations sur lequel le test doit faire effet : "))#nombre de générations sur lequel le test doit faire effet
population = []
pop = []
n_pop = []
tabEnfant = []
tabDeTri = []
pourcentageDeMutations = int(input("Entrez le pourcentage de mutation : "))#pourcentage de mutation


x = np.random.randint(0,50,N)
y = np.random.randint(0,50,N)
chemin = np.arange(N)
plt.scatter(x,y,s=70)


creation(population, M, pop)


pop_Sorted = sorted(pop, key = lambda x: x[1], reverse = False)
for i in range(1,genMax):
    n_pop = []
    pop = []
    pop_Sorted = nextGen(i, n_pop, pop, pop_Sorted,M)
    for j in range(0,len(pop_Sorted)):
        randomX = rd.randint(0, 100)
        mutates = mutate(pourcentageDeMutations, 100, randomX)
        mutation(mutates, pop_Sorted,rd.random(),j)
        st = str(mutates)
    string = 'Gen : ' + str(i) +' '+ str(pop_Sorted[0][0])+ ' mutation = '+ st
    tuples = (string,pop_Sorted[0][1])
    tabDeTri.append(tuples)
  
tabDeTriSorted = sorted(tabDeTri,key = lambda x: x[1], reverse = False)  
pltTab1 = []
pltTab2 = []
for i in range(0,len(x)):
    pltTab1.append(x[i])
    pltTab2.append(y[i])

plt.plot(x, y, 'r->')
plt.show()

print("Le chemin le plus court est celui de la :",tabDeTriSorted[0])
    



