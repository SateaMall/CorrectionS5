from matplotlib import pyplot as plt
from matplotlib import collections  as mc
from math import *
from random import *
from time import *

### Dessins ###

def __points(ax, Points, color, markersize):
	ax.plot(*zip(*Points),marker='.',markersize=markersize,linestyle='',color=color)

def __aretes(ax, Points, Adj, color, markersize, lw):
	liste = []
	for s in Adj:
		for v in Adj[s]:
			liste.append([Points[s], Points[v]])
	lc = mc.LineCollection(liste, linewidth=lw, color=color)
	ax.add_collection(lc)
	ax.autoscale()

def __parcours(ax, Points, Parcours, Adj, color1, color2, markersize):
	n = len(Points)
	liste1 = []
	liste2 = []
	for i in range(len(Parcours)):
		if len(Adj) == 0 or Parcours[(i+1)%n] in Adj[Parcours[i]]: 
			liste1.append([Points[Parcours[i]], Points[Parcours[(i+1)%n]]])
		else:
			liste2.append([Points[Parcours[i]], Points[Parcours[(i+1)%n]]])
	lc1 = mc.LineCollection(liste1, linewidth=1, color=color1)
	lc2 = mc.LineCollection(liste2, linewidth=1, color=color2)
	ax.add_collection(lc1)
	ax.add_collection(lc2)
	ax.autoscale()

	if len(Parcours) < 100:
		for s in range(len(Parcours)):
			ax.annotate(str(s+1), Points[Parcours[s]])

def dessinPoints(Points, color="C0",markersize=5):
	fig, ax = plt.subplots()
	__points(ax, Points, color, markersize)
	plt.axis('equal')
	plt.show()

def dessinGraphe(Points, Adj, color="C0",markersize=5):
	fig, ax = plt.subplots()
	__points(ax, Points, color, markersize)
	__aretes(ax, Points, Adj, color, markersize, 1)
	plt.axis('equal')
	plt.show()

def dessinArbre(Points, Arbre, Adj={}, color1="C0",color2="C1",markersize=5):
	fig, ax = plt.subplots()
	__points(ax, Points, color1, markersize)
	__aretes(ax, Points, Adj, color1, markersize, 0.5)
	__aretes(ax, Points, Arbre, color2, markersize,1)
	plt.axis('equal')
	plt.show()



def dessinParcours(Points, Parcours, Adj = {}, color1="C0", color2="C1", markersize=5):
	n = len(Points)
	assert sorted(Parcours) == list(range(n)), "le parcours ne visite pas chaque sommet une fois et une seule"

	fig, ax = plt.subplots()
	__points(ax, Points, color1, markersize)
	if len(Adj) > 0: __aretes(ax, Points, Adj, 'gray', markersize, .5)
	__parcours(ax, Points, Parcours, Adj, color1, color2, markersize)

	plt.axis('equal')
	plt.show()

#Exo 1
#1)

def distance( p1, p2):
	return sqrt( pow(p2[0]-p1[0],2) + pow(p2[1]-p1[1],2) )

A, B, C = (121,77),(48,70),(12,72)
print("Exercice 1: \n", )
print("1) \n")
print(distance(A,B),distance(A,C),distance(B,C))
print("----------------------- \n2) \n")


#2)

def aretes(P):
	aretes = []
	for i in range(0,len(P)):
		for j in range(i+1,len(P)):
			aretes.append((i,j,distance(P[i],P[j])))
	return aretes

P = [(6 ,20) ,(67 ,18) ,(96 ,4) ,(32 ,45)]
print ( aretes ( P ))

print("----------------------- \n3) \n")

#3)

def pointsAleatoires(n, xmax, ymax):
	P=[]
	for i in range(0,n):
		P.append((uniform(0,xmax),uniform(0,ymax)))
	return P

print ( pointsAleatoires (3 , 10 , 20))

print("----------------------- \n4) \n")

#4)

print("affichage graphe point aléatoire : ")
#dessinPoints(pointsAleatoires (3 , 10 , 20))
print("affichage fermé")
print("----------------------- \n5) \n")

#5)

def listesAdjacente(P):
	dico = {}
	for i in P:
		if i[0] not in dico:
			dico[i[0]] = [i[1]]
		if i[1] not in dico:
			dico[i[1]] = [i[0]]

		if i[1] not in dico[i[0]]:
			dico[i[0]].append(i[1])
		if i[0] not in dico[i[1]]:
			dico[i[1]].append(i[0])
	return dico

A = [(0 ,1) ,(0 ,2) ,(0 ,3) ,(1 ,2) ,(1 ,3) ,(2 ,3)]
print ( listesAdjacente ( A ))
print("----------------------- \n6) \n")

#6)

print("affichage graphes avec arêtes :")
#dessinGraphe(P, listesAdjacente(A))
P2 = pointsAleatoires(6,25,25)
#dessinGraphe(P2, listesAdjacente(aretes(P2)))

print("affichage fermé")
print("----------------------- \nExercice 2: \n")
print("1)")

#Exercice 2)
#1)

def arbreCouvrant(Points):
	G=aretes(Points)
	G=sorted(G, key=lambda distance:distance[2])
	T=[]
	i=0
	comp=[]
	for x in range(len(G)):
		comp.append(i)
		i+=1
	for uv in G:
		if comp[uv[0]]!=comp[uv[1]]:
			T.append(uv)
			aux=comp[uv[0]]
			for w in range(len(G)):
				if comp[w]==aux: 
					comp[w]=comp[uv[1]]
	return T

A = [(6 ,20) ,(67 ,18) ,(96 ,4) ,(32 ,45)]
G = []
for i in arbreCouvrant ( A ):
	G.append(i[:2])
print(G)

print("----------------------- \n2) \n")

#2)
print("ouverture dessin graphe")
#dessinGraphe(A, listesAdjacente(aretes(A))) 
print("ouverture dessin arbre")
#dessinArbre(A, listesAdjacente(G))
print("fin exercice")

print("----------------------- \n3) \n")
#3)

st = time()
#arbreCouvrant(pointsAleatoires(763,25,25))
et = time()
print("temps écoulé : ",et-st," secondes")
print("entre 760 et 765")
print("----------------------- \nExercice 3: \n")
print("----------------------- \n1) \n")

#Exercice 3)
#1)

def PeP(G):
	P = [0]
	C = []
	
	while P != []:
		s = P.pop()
		C.append(s)
		for v in G[s]:
			if v not in C + P:
				P.append(v)
	return C

print("----------------------- \n2) \n")
#2)

P3 = [(6 ,60) ,(67 ,62) ,(96 ,76) ,(32 ,35) ,(70 ,39) ,(98 ,24) ,(129 ,30) ,(121 ,3) ,(48 ,10) ,(12 ,8)]
arbrecouvrantp3 = []
for i in arbreCouvrant ( P3 ):
	arbrecouvrantp3.append(i[:2])
print(arbrecouvrantp3)

pepp3 = PeP(listesAdjacente(arbrecouvrantp3))

#dessinParcours(P3,pepp3)
print("----------------------- \n3) \n")
#3)

def VDC(Points):
	A = arbreCouvrant(Points)
	P = PeP(listesAdjacente(A))
	listefinale = []
	for i in range(0,len(P)):
		listefinale.append(Points[P[i]])
	return listefinale

print(P3)
print(VDC(P3))

#dessinParcours(VDC(P3),PeP(listesAdjacente(arbreCouvrant(VDC(P3)))))

print("----------------------- \n4) \n")

st = time()
VDC(pointsAleatoires(772,25,25))
et = time()
print("temps écoulé : ",et-st," secondes")
print("entre 770 et 775")