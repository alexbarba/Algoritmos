# coding=utf-8
#Programación Dinámica:
#Calcular la subsecuencia más larga

A='xyxxzxyzxy'
B='zxzyyzxxyxxz'


def SubsecuenciaMax(A,B):
	X=''
	n = len(A)
	m = len(B)
	subsec=''
	import numpy
	L = numpy.zeros(shape=(n+1,m+1))
	#print M
	
	for i in range(n):
		for j in range(m):
			if A[i]==B[j]:
				L[i+1][j+1]=L[i][j]+1
				
			elif A[i]!=B[j]:
				L[i+1][j+1]=max(L[i+1][j],L[i][j+1])
	
	for i in range(len(L[n])):
		if L[n][i]>L[n][i-1]:
			subsec+=A[i-1]
			
	return L[n][m], subsec

	

print SubsecuenciaMax(A,B)
