from random import *
from matplotlib import pyplot as plt
from math import *

#Exercice 1)

#1)
# i)

def entiersAleatoires(n,a,b):
	listerandom = []
	for i in range(0,n):
		listerandom.append(randint(a,b))
	return listerandom


# ii)

def entiersAleatoires2(n,a,b):
	listerandom = []
	for i in range(0,n):
		listerandom.append(randrange(a,b))
	return listerandom


# iii)

L1 = entiersAleatoires(1000,1,100)
L2 = entiersAleatoires2(1000,1,100)
#plt.hist(L1, bins=100)
#plt.show()
#plt.hist(L2, bins=100)
#plt.show()



# 2)
# i)
def flottantsAleatoires(n):
	listerandom = []
	for i in range(0,n):
		listerandom.append(random())
	return listerandom

L3 = flottantsAleatoires(5)

# ii)

def flottantsAleatoires2(n,a,b):
	listerandom = []
	for i in range(0,n):
		listerandom.append(uniform(a,b))
	return listerandom

L4 = flottantsAleatoires2(1000,-3,10)

# iii)

#plt.plot(L4)
#plt.show()

# 3)
# i)

def pointsDisque(n):
	listex=[]
	listey=[]
	compte=0
	while compte<n:
		x = uniform(-1,1)
		y = uniform(-1,1)
		if (pow(x,2)+pow(y,2)) <= 1:
			listex.append(x)
			listey.append(y)
			compte+=1
	plt.scatter(listex, listey)
	plt.show()

pointsDisque(1000)

# ii)

def pointsDisque2(n):
	listex=[]
	listey=[]
	compte=0
	while compte<n:
		x = uniform(-1,1)
		y = uniform(-1,1)
		if (pow(x,2)+pow(y,2)) >= 1:
			y = uniform(-1,1)
		else:
			listex.append(x)
			listey.append(y)
			compte+=1

	plt.scatter(listex, listey)
	plt.show()

pointsDisque2(1000)

# iii)

def pointsDisque3(n):
	liste=[]
	for i in range(0,n):
		theta = uniform(0,pi/2)
		r = uniform(0,1)

		liste.append((r*cos(theta),r*sin(theta)))

	return liste

# iv)

def affichagePoints ( L ):
	X = [x for x,y in L]
	Y = [y for x,y in L]
	plt.scatter(X,Y,s=1)
	plt.axis("square")
	plt.show()

affichagePoints(pointsDisque3(10000))

# 4)
# i)
