#coding=utf-8
def subconjunto(A, t):
	n = len(A)
	
	
	import numpy
	L = numpy.zeros(shape=(n,n+1))
	for i in range(n):
		L[0][i]=A[i]
	#print L
	for i in range(1,n+1):
		for j in range(n-i):
			L[i][j]=L[i-1][j]+L[0][i+j]
	print L
	subconjuntos, subconjuntoMax = maxLen(L, t, A)		
	return subconjuntos, subconjuntoMax

def maxLen(L, t, A):
	n=len(L)
	
	subconjuntos=[]
	maxim=[]
	for i in range(n+1):
		for j in range(n-i):
			if L[i][j]==t:
				#print i, j
				subconjuntos.append(A[j:j+i+1])
				if len(maxim)<len(A[j:j+i+1]):
					maxim=A[j:j+i+1]
	return subconjuntos ,maxim
				
		
A=[6, 1, 1, 1, 3, 3, 4, 5]

t=6
subconjuntos, subconjuntoMax= subconjunto(A, t)
print subconjuntos
print subconjuntoMax
