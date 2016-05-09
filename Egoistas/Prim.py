# coding=utf-8
import numpy as np

archivo = 'grafos'
def Prim(E):
	n=len(E)
	V=range(n)
	Y=[0]
	F=[range(n) for i in range(n)]
	for i in range(n):
		for j in range(n):
			F[i][j]=float('inf')
	
	for i in range(n):
		#Criterio de selección
		posx, posy = Min(E,Y)
		#viabilidad
		pos=NotInY(posx,posy,Y)
		if pos: 
			Y.append(pos)
			F[posx][posy]=E[posx][posy]
			F[posy][posx]=E[posx][posy]
			E[posx][posy]=float('inf')
			
			#Verificación de solución
			if len(Y)==len(V):
				return F
		else:
			E[posx][posy]=float('inf')
			i-=1
	return F
	
def NotInY(posx,posy,Y):
	if posx not in Y:
		return posx
	elif posy not in Y:
		return posy
	else:
		return 0

def Min(E,Y):
	minim=float('inf')
	mini=0
	minj=0
	for i in range(len(Y)):
		for j in range(i+1,len(E)):
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
print 'Esta es la solución Prim (inicializando en 0):'
print np.array( Prim(matriz),dtype='double')
