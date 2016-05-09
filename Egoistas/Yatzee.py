import time
def Yatzee(values):
	DadosEnJuego = 5
	if len(values)>DadosEnJuego:
		return "La cantidad de valores no coincide con la cantidad de dados, intente nuevamente"
	#ordenamos los valores
	#values = RadixSort(values)
	cubos = [0] * (DadosEnJuego+2)
	
	maximo=0
	for value in values:
		cubos[value]+=value
		if cubos[value]>maximo:
			maximo=cubos[value]
	
	return maximo

	
values = [4,4,5,6,6]

inicial=time.clock()
print Yatzee(values)
final=time.clock()
print ("Tiempo De Ejecucion: %f"%((final - inicial)*1000)+"(ms)")

