def quicksort(vector, inicio, fin):
    pri = inicio
    ult = (fin-1)
    pivot = fin
    while (pri < ult):
        while (vector[pri] < vector[pivot]) and (pri < ult):
            pri += 1
        while(vector[ult] > vector[pivot]) and (ult > pri):
            ult -= 1
        if (pri < ult):
            vector[pri], vector[ult] = vector[ult], vector[pri]
    if (vector[pivot] < vector[pri]):
        vector[pri], vector[pivot] = vector[pivot], vector[pri]
    if (inicio < pri):
        quicksort(vector, inicio, fin - 1)
    if (ult > pri):
        quicksort(vector, inicio + 1, fin)


def bbin(vector,busc,pri,ult):
    pos = -1
    if (pri <= ult):
        med = (pri + ult) //2
        if (vector[med] ==  buscado):
            return (med)
        elif (vector[med] < buscado):
            return (bbin(vector,busc,med+1,ult))
        else:
            return (bbin(vector,busc,med-1,ult))
    else:
        return (-1)

datos = [11, 3, 10, 7, 5, 20, 4, 22, 81, 25, 30, 81]

quicksort(datos,0,len(datos)-1)
print (datos)

bbin(datos,5,0,len(datos)-1)