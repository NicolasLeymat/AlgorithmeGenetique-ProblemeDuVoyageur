import random
import numpy as np




def Mutation(pourcentage, CONSTANTEL) :
    a = random.randint(0,CONSTANTEL)
    #Simple if pour verifier si la mutation sera effectuer ou pas
    if a < pourcentage :
        #on retourne oui si la mutation doit etre effectuer
        return True
    else :
        #On return non si la mutation n'as pas lieu d'etre
        return False



def K(CONSTANTEL):
    #bete random pick de k pour la séparation des bits des parents
    k = random.randint(1,CONSTANTEL)
    return k

#Création des fonction pour la création des parents
def creationParents(CONSTANTEL) :
    i = 0
    p1 = []
    #Simple boucle while pour remplir le tableau contenatn les bits du parent 
    while i < CONSTANTEL :
        #Selection pseudo aleatoire des bits entre 0 et 1
        p1.append(random.randint(0,1))
        #iteration du parametre permetant de sortir de la boucle
        i+=1
    #Retour du tableau contenant les bits
    return p1

#Calcul le fitness d'un individu
def fitness(tab):
    x = 0
    for i in range(0,len(tab)):
        x += tab[i]
    return x


#Fonction pour passer à la prochiane génération
def nextGen(gen,tabP, tabE,tabSorted, Dims):
    tabP.append(tabSorted[0][0])
    for w in range(0,int(Dims/2),1):
        randomInteger = random.randint(1,N-1)
        popI = tabSorted[w][0]
        popJ = tabSorted[w+1][0]
        tabP.append(crossover(popI,popJ,randomInteger))
    for i in range(1, len(tabP)):
        tabP[i] = tabP[i].tolist()
    
    
    fillChemin(tabP)


    for i in range(0,Dims):
        fit = fitness(tabP[j])
        tuples = (tabP[j],fit)
        tabE.append(tuples)
    tabSorted = sorted(tabE,key = lambda x: x[1], reverse = True)
    return tabSorted
    
#fonction pour remplir le tableau enfants
def fillChemin(tab):
    for i in range(len(tab),Dim):
        tab.append(creationParents(N))
        
#fait un crossover des 2 tableau en parametre en fonction d'un nombre x random
def crossover(t1,t2,x):
    tNew = np.append(t1[:x],t2[x:])
    return tNew

Dim = int(input("Entrez la dimension su test : "))
N = int(input("Entrez le nombre de génomes voulu : "))
PourcentageDeMutation = int(input("entrez le pourcentage de mutation : "))
NombreDeGenerations = int(input("Entrez le nombre de génération du test : "))
tabParents = []
tabEnfants = []
tabFinal = []


for i in range(0,Dim):
    tabParents.append(creationParents(N))

for j in range(0,len(tabParents)):
    fit = fitness(tabParents[j])
    tuples = (tabParents[j],fit)
    tabEnfants.append(tuples)
    
tabEnfants_Sorted = sorted(tabEnfants, key = lambda x: x[1], reverse = True)

for i in range(1,NombreDeGenerations):
    tabEnfants = []
    tabParents = []
    tabEnfants_Sorted = nextGen(i,tabParents,tabEnfants,tabEnfants_Sorted,Dim)
    
    string = 'Gen : ' + str(i) + ' ' + str(tabEnfants_Sorted[0][0])
    tuples = (string,tabEnfants_Sorted[0][1])
    tabFinal.append(tuples)

tabFinalSort = sorted(tabFinal,key = lambda x: x[1], reverse = True)
print("Le meilleur enfant est celui la : ", tabFinalSort[0])



