# coding=utf-8
import numpy as np

archivo = 'grafos'
def Kruskal(E):
	n=len(E)
	V=range(n)
	Y=[]
	F=[range(n) for i in range(n)]
	for i in range(n):
		for j in range(n):
			F[i][j]=float('inf')
	
	for i in range(n):
		#Criterio de selección
		posx, posy = Min(E)
		#viabilidad
		pos=NotInY(posx,posy,Y)
		if pos: 
			F[posx][posy]=E[posx][posy]
			F[posy][posx]=E[posx][posy]
			E[posx][posy]=float('inf')
			
			
			#Verificación de solución
			if len(Y)==len(V)-1:
				return F
		else:
			E[posx][posy]=float('inf')
			i-=1
	return F
	
def NotInY(posx,posy,Y):
	if posx in Y and posy in Y:
		return 0
	elif posx not in Y:
		Y.append(posx)
		return 1
	elif posy not in Y:
		Y.append(posy)
		return 1

def Min(E):
	minim=float('inf')
	mini=0
	minj=0
	n=len(E)
	for i in range(n):
		for j in range(i+1,n):
			if E[i][j]<minim:
				minim=E[i][j]
				mini=i
				minj=j
	return mini,minj


def leertxt():
	f=open(archivo,'r')
	linea=f.readline()
	lineas=[]

	while linea!="":
		lineas.append(map(float,linea.split(' ')[:-1]))
		linea=f.readline()
		
	f.close()
	return lineas

matriz = leertxt()

#Imprimo matriz original
print 'Este es el grafo original:'
print np.array(matriz,dtype='double')
print 'Esta es la solución Kruskal:'
print np.array( Kruskal(matriz),dtype='double')
