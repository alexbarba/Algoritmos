#Encuentra el orden de multiplicacion optimo y almacena la matriz de operaciones
def OrdenOptimo(A):
	import numpy
	A = MatrizToArray(A)
	n=len(A)
	M = numpy.zeros(shape=(n-1,n-1))
	orden=''
	
	for i in range(n-2):
		for j in range(n-2-i):
			if M[j][j+i]<M[j+1][j+i+1]:
				M[j][j+i+1]=M[j][j+i]+A[j]*A[j+i+1]*A[j+i+2]
				orden+=str(j+i+i-1)
			else:
				M[j][j+i+1]=M[j+1][j+i+1]+A[j]*A[j+1]*A[j+i+2]
				orden+=str(j)
	
	
	orden = orden[1:n-1]
	return M, StringOrden(orden)
	

#Se encarga de decodificar el orden en que se debe multiplicar la matriz
def StringOrden(Orden):
	OrdenMatrices=''
	for i in range(len(Orden)+1):
		OrdenMatrices += str(unichr(i+65))
	#Definimos los parentesis iniciales
	temp = int(Orden[0])
	OrdenMatrices = OrdenMatrices[:temp]+'('+OrdenMatrices[temp:temp+2]+')'+OrdenMatrices[temp+2:]
	
	for i in range(1,len(Orden)-1):
		LParen = OrdenMatrices.find('(')
		RParen = OrdenMatrices.rfind(')')
		#pos=int(Orden[i])-temp
		if temp-int(Orden[i])==1:
			OrdenMatrices = OrdenMatrices[:LParen-1]+'('+OrdenMatrices[LParen-1:RParen]+')'+OrdenMatrices[RParen:]
		elif int(Orden[i])-temp==1:
			OrdenMatrices = OrdenMatrices[:LParen]+'('+OrdenMatrices[LParen:RParen+2]+')'+OrdenMatrices[RParen+2:]
		temp = int(Orden[i])
	
	return OrdenMatrices
	
#Esta funcion convierte un arreglo de duplas a un vector
def MatrizToArray(A):
	if len(A[0])==1:
		return A
	elif len(A[0])==2:
		B = [0]*len(A)
		for i in range(len(A)):
			B[i]=A[i][0]
		B.append(A[i][1])
		return B
	else:
		return "Error"

	

#A((BC)D)
#A = [ [20, 2], [2, 30], [30, 12], [12, 8] ]
#(A(BC))D 
A = [ [13, 5], [5, 89], [89, 3], [3, 34] ]
#((AB)(CD))
#A = [ [13, 97], [97, 12], [12, 96], [96, 34] ]
#((AB)C(DE))
#A = [ [13, 97], [97, 12],[12,12] ,[12, 96], [96, 34] ]
#A=[ [5,2], [2,3], [3,4] ]

#print str(TablaCantidadOp(A)) + '\n'
#print Diagonal1(A)
M, orden = OrdenOptimo(A)
print orden
print M

#print 'Cantidad de multiplicaciones minimas: '+str(op)+'\nOrden de multiplicacion: '+orden
#print '\n\nNOTA: Orden de multiplicaciones en beta. EL ACOMODO DE LAS MATRICES SOLO ES ACERTADO SI HACE MOVIMIENTOS DE 1 EN 1 HACIA IZQUIERDA O DERECHA\nEjemplo: En un caso donde el orden es ((AB)C(DE)) no lo decodificaria de dicho modo'


