import matplotlib.pyplot as plt
from random import *
import time

###########################################

def TableauAuHasard(n):
	TabHasard=[]
	for i in range(0,n):
		TabHasard.append(randrange(0,n*n))
	return TabHasard


def TriFusion(n,T):
	if n>1:
		n1=n//2 
		n2=n-n1 
		T1=T[0:n1]
		T2=T[n1:n]
		TriFusion(len(T1), T1)
		TriFusion(len(T2), T2)
		return Fusion(len(T1), len(T2), T1, T2, T)

def Fusion(n1, n2, T1, T2, T):
	i1 = 0
	i2 = 0
	i = 0
	for iS in range(n1+n2):
		if ( i1 >= n1):
			T[iS]= T2[i2]
			i2 = i2+1
		elif(i2>=n2):
			T[iS]= T1[i1]
			i1 = i1+1
		elif(T1[i1]<T2[i2]):
			T[iS]= T1[i1]
			i1 = i1+1
		else:
			T[iS]= T2[i2]
			i2=i2+1


def TriBulles(n,T):
	for i in range(n, 1 , -1):
		for j in range(0,i-1):
			if T[j] > T[j+1]:
				T[j],T[j+1] = T[j+1],T[j]

def Quicksort(n,T):
	np = 0
	T0 = []
	T1 = []
	if n <= 1 : 
		return T
	p = T[randint(0,n-1)]
	for i in range(0,n):
		if T[i] == p:
			np = np+1
		if T[i] < p:
			T0.append(T[i])
		if T[i] > p:
			T1.append(T[i])
	T0 = Quicksort(len(T0),T0)
	T1 = Quicksort(len(T1),T1)
	return T0 + np * [n] + T1

#######Programme Principal########

choix=int(input("Taper 1 pour un test sur un exemple simple, 2 pour un comparatif TriFusion/TriBulles/Quicksort: "))
if choix==1:
	n=6
	T=TableauAuHasard(n)
	print("Tableau de depart: ",T)

	Tbulles=T.copy()
	TriBulles(n, Tbulles)
	print("Apres tri bulles: ",Tbulles)

	Tfusion=T.copy()
	print("Tableau de depart: ",Tfusion)
	TriFusion(n, Tfusion)
	print("Apres tri fusion: ",Tfusion)

	Tquick=T.copy()
	print("Tableau de depart: ",Tquick)
	Quicksort(n, Tquick)
	print("Apres QuickSort",Tquick)
	
else:
	#Valeurs de n choisies    
	abscisses = [n for n in range(1,1000,10)]
	#Temps de calcul
	tps1 = []
	tps2 = []
	tps3 = []
	for n in range(1,1000,10):
		T=TableauAuHasard(n)
		T1=T.copy()
		t=time.time()
		TriBulles(n, T1)
		tps1.append(time.time()-t)
		T2=T.copy()
		t=time.time()
		TriFusion(n, T2)
		tps2.append(time.time()-t)
		T3=T.copy()
		t=time.time()
		Quicksort(n, T3)
		tps3.append(time.time()-t)
	
	#Tracé
	plt.plot(abscisses, tps1, label="Tri bulles")
	plt.plot(abscisses, tps2, label="Tri Fusion")
	plt.plot(abscisses, tps3, label="Quicksort")
	plt.legend(loc="upper left")
	plt.show()
