#ideone
import random
import time
import math

def RadixSort(lista):
    max_Len = -1
    for number in lista: # Se encuentran los numeros mas largo
        num_Len = int(math.log10(number)) + 1
        if num_Len > max_Len:
            max_Len = num_Len
    cubos = [[] for i in range(0, 10)] # el cubo para cada digito
    for digit in range(0, max_Len):
        for number in lista:
            cubos[number / 10**digit % 10].append(number)
        del lista[:]
        for bucket in cubos:
            lista.extend(bucket)
            del bucket[:]
    return lista 
  
def reset():
	TamLista = 1000000
	lista = []
	
	for i in range(TamLista):
		lista.append(random.randint(0,10000))
	inicial=time.clock()
	for i in range(10):
		RadixSort(lista)
	
	Tiempo_Termina1 = time.clock()

    
	print ("Tiempo De Ordenamiento: %f"%(Tiempo_Termina1 - inicial))
    
    
reset()
