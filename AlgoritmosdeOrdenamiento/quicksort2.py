def quicksort(L, first, last):
    # definimos los indices y calculamos el pivote
    i = first
    j = last    
    pivote = (L[i] + L[j]) / 2

    # iteramos hasta que i no sea menor que j
    while i < j:
        # iteramos mientras que el valor de L[i] sea menor que pivote
        while L[i] < pivote:
            # Incrementamos el indice
            i+=1
        # iteramos mientras que el valor de L[j] sea mayor que pivote
        while L[j] > pivote:
            # decrementamos el indice
            j-=1
        # si i es menor o igual que j significa que los indices se han cruzado
        if i <= j:
            # creamos una variable temporal para guardar el valor de L[j]
            x = L[j]
            # intercambiamos los valores de L[j] y L[i]
            L[j] = L[i]
            L[i] = x
            # incrementamos y decrementamos i y j respectivamente
            i+=1
            j-=1

    # si first es menor que j mantenemos la recursividad
    if first < j:
        L = quicksort(L, first, j)
    # si last es mayor que i mantenemos la recursividad
    if last > i:
        L = quicksort(L, i, last)

    # devolvemos la lista ordenada
    return L
A=[1, 4, 8, 2, 6, 9, 3, 5]
print quicksort(A, 0, len(A)-1)
