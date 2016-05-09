import time
def VerificarUsername(A, username):
	#Definimos la maxima longitud del username
	MaxLong=50
	
	#Eliminamos los caracteres no validos
	username=DelCaracteresEspeciales(username)
	
	#Eliminamos los 0 no validos
	username=EliminaCeros(username)
	
	#Si no es alfanumerico lo convertimos en alfanumerico		
	if not(username.isalnum()):
		username='a'+username
	
	#Verificamos la longitud del username
	username = MaximaLongitud(username,MaxLong)
	
	#Encuentra si el username se encuentra en la lista, si no, devuelve el username valido
	if not(A.count(username)):
		return username
		
	#Ordena la lista
	#A.sort()
	#MSD_radix_string_sort(A, 1)
	
	#eliminamos los ultimos digitos
	while '0123456789'.count(username[-1]):
		username = username[:-1]
	if not(A.count(username)):
		return username
		

	for j in range(1,100000):
		#si al incrementarle el numero superamos nuestra cantidad maxima de caracteres, eliminamos la ultima letra
		if len(username+str(j))>=MaxLong:
			username = DelUltimaLetra(username,MaxLong)
		if not(A.count(username+str(j))):
			return username+str(j)
	
	
	return 0

def DelUltimaLetra(username):
	username =username[:DigEnd(username)-1]
	return username
							
def MaximaLongitud(username, MaxLong):
	while len(username)>MaxLong:
		username=username[:-1]
	return username
	
def EliminaCeros(username):
	#si empieza con 0, los elimina
	while username[0]=='0': username=username[1:]
	#Si sus ultimos digitos empiezan con 0 los elimina
	if -DigEnd(username)==username[DigEnd(username):].count('0'):
		while username[-1]=='0': username = username[:-1]
	
	#Elimina cuantos 0 invalidos queden
	while username[DigEnd(username)]=='0':
		username = username[:DigEnd(username)]+username[DigEnd(username)+1:]
	return username

#Cuento cuantos digitos tengo al final de mi array
def DigEnd(name):
	i=-1
	while name[i].isdigit():
		i-=1
	return i+1
		
def DelCaracteresEspeciales(username):
	from string import ascii_letters
	ascii_chars=ascii_letters + '0123456789'
	
	for l in username:
		if ascii_chars.find(l)==-1:
			username=username.replace(l,"")
			
	return username	
	
	
A = ['MasterOfDisaster', 'DingBat', 'Orpheus', 'WolfMan', 'MrKnowItAll', '234bart2342345254330000']
B= ['bart', 'bart1','bart2','bart3','bart4','bart5','bart6','bart7','bart8','bart9']
username='00000%%$%&$&%234bart000234234525433001'
username2='bart1'

inicial=time.clock()
print VerificarUsername(B, username2)
final=time.clock()
print ("Tiempo De Ejecucion: %f"%((final - inicial)*1000)+"(ms)")
'''
Este algoritmo tiene el tiempo de ejecucion mas largo de los 3 ejercicios, pues 
su complejidad fue mucho mayor debido a la implementacion de muchos mas metodos:
	1. El primer paso fue eliminar los caracteres especiales que no son admitidos,
	esto tuvo un tiempo lineal O(kn) donde k es la cantidad de caracteres validos 
	y n la cantidad	de caracteres de la cadena enviada, asi como un espacio en memoria
	adicional para el arreglo k.
	2. El segundo paso fue eliminar los ceros no validos, cuando empieza con cero, o cuando
	lo contiene como sufijo. Con un costo en el peor de los casos O(n2+n+m), donde n es la
	cantidad de digitos con la que termina y m la cantidad de ceros con la que empieza,
	siendo el peor	de los casos que todos los digitos sean 0
	3. El tercer paso consiste en eliminar todos los caracteres que sobrepasen el tamaño
	maximo permitido, teniendo un costo de O(n) donde n es la cantidad de caracteres excedentes.
	4. Se recorre todo el array en busca de un valor que coincida con el username ingresado, siendo
	el peor de los casos que este no se encuentre con O(kn) donde n es el tamaño del array y k el
	maximo tamaño de caracteres.
	5. Si el username se repite, empezamos una busqueda exhaustiva de un username valido donde
	al username le vamos a eliminar los ultimos valores enteros para empezar el reconteo y se
	ira sumando un valor entero al final para volver a recorrer el array, y si este superara la maxima
	longitud permitida se eliminaria la ultima letra del username para asi poder seguir incrementando
	el valor entero. El calculo se vuelve un poco mas complejo siendo aproximadamente O(kn*10eM), el
	mismo tiempo que en el paso 4 multiplicado por 10eM donde M es la cantidad maxima de enteros
	permitidos siendo el peor de los casos que haya 10eM nombres iguales.
	

	'''
	
	
