import time
def CalculaGananciaDelDia(DineroEnJuego,GananciaDolar, MargenVictoria):
	error = "El tamano de las entradas o su tipo no son correctas"
	#Reviso que los tamanios coincidan
	if len(DineroEnJuego)!=len(GananciaDolar) or len(DineroEnJuego)-1<MargenVictoria:
		return error
	#reviso que todos sean enteros
	else:
		for x in DineroEnJuego:
			if type(x)!=int:
				return error
		for x in GananciaDolar:
			if type(x)!=int:
				return error
		if type(MargenVictoria)!=int:
			return error
	
	EntradasNetas=0
	
	CantidadAPagar=DineroEnJuego[MargenVictoria]*GananciaDolar[MargenVictoria]/100+DineroEnJuego[MargenVictoria]
	
	for i in range(len(DineroEnJuego)):
		EntradasNetas+=DineroEnJuego[i]		
	
	GananciasNetas = EntradasNetas-CantidadAPagar
	return GananciasNetas
	

DineroEnJuego=[10, 20, 30]
GananciaDolar=[20, 30, 40]
MargenVictoria=1

inicial=time.clock()
print CalculaGananciaDelDia(DineroEnJuego, GananciaDolar, MargenVictoria)
final=time.clock()
print ("Tiempo De Ejecucion: %f"%((final - inicial)*1000)+"(ms)")

'''
La complejidad de este algoritmo es lineal pues solamente tiene que hacer la suma de
los enteros de un array, y unos pocos calculos constantes y almacenar dos arrays y variables
constantes. Entonces O(n+c).
'''
