from random import *
from matplotlib import pyplot as plt
from math import *
from time import *

# 1)
# i)
def eltMajDet(T):
	debut = time()
	for i in range(0,len(T)):
		compte = 0
		for j in range(0,len(T)):
			if T[i] == T [j]:
				compte += 1
		if compte >= len(T)/2:
			print(time()-debut)
			return T[i]
	

L=[1,2, 10, 2, 2,2,3,8,5,2,2,2,2,7,9]

#print(eltMajDet(L))

# ii)
def eltMajProba(T):
	debut = time()
	while 1:
		compte = 0
		rand = choice(T)
		for i in range(0,len(T)):
			if T[i] == rand:
				compte += 1
		if compte >= len(T)/2:
			print(time()-debut)
			return rand


#print(eltMajProba(L))

# iii)

print("exo 1, iii)")

def tabAlea(n, a, b, k):
	liste = []
	m = randint(a,b)
	for i in range(0,k):
		liste.append(m)
	for j in range(0,n-k):
		liste.append(randint(a,b))
	shuffle(liste)
	return liste

L2 = tabAlea(11,0,6,6)
print(L2)
print(eltMajProba(L2))
print(eltMajDet(L2))


print("-----------------------")
print("exo 1, iv)")

def tabDeb(n, a, b, k):
	liste = []
	m = randint(a,b)
	for i in range(0,k):
		liste.append(m)
	for j in range(0,n-k):
		liste.append(randint(a,b))
	return liste


def tabFin(n, a, b, k):
	liste = []
	m = randint(a,b)
	for j in range(0,n-k):
		liste.append(randint(a,b))
	for i in range(n-k,n):
		liste.append(m)
	return liste

L3 = tabDeb(11,0,6,6)
L4 = tabFin(11,0,6,6)

print(L3)
print("probabiliste :")
print(eltMajProba(L3))
print("déterministe :")
print(eltMajDet(L3))

print(L4)
print("probabiliste :")
print(eltMajProba(L4))
print("déterministe :")
print(eltMajDet(L4))

print("-----------------------")
print("exo 2, i)")

def contientEltMaj(T,m):
	for i in range(0,m):
		compte = 0
		maj = choice(T)
		for j in range(0,len(T)):
			if T[j] == maj:
				compte +=1
		if compte >= len(T)/2:
			return True
	return False

def testContient(n,a,b,k,m,N):
	tab = tabAlea(n, a, b, k)
	nbtrue = 0
	for i in range(0,N):
		if contientEltMaj(tab,m):
			nbtrue += 1
	return (nbtrue/N)*100

print("pourcentage de réussite :", end=" ")
print(testContient(1000,0,10,500,1,1000),end="");print("%")