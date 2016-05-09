
def agendar(t):
	t.sort()
	tiempo_total = 0
	
	for i in range(len(t)):
		tiempo_total+=sum(t[:i+1])
		
	return t, tiempo_total
	
tiempos = [5, 10, 4]
print agendar(tiempos)
