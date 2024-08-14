def encontrarSUMA(lista, numero):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == numero:
                return True
    return False

def encontrarSumaExtremos(lista, numero):
    izq, der = 0, len(lista) - 1
    while izq < der:
        sumaActual = lista[izq] + lista[der]
        if sumaActual == numero:
            return True
        if sumaActual < numero:
            izq += 1
        else:
            der -= 1
    return False

lista = [1,3,1,6,1,10,1]
print(encontrarSUMA(lista, 13))
print(encontrarSumaExtremos(lista, 13))

def ordenarNumeros(lista):
    for i in range(len(lista) - 1): #recorremos la lista desde la pos 0 hasta la penultima
        smallest = i #tomamos el menor valor hasta el momento
        j = i + 1 #creamos otro puntero desde una posicion más adelante que i
        for j in range(len(lista)): #avanzamos el puntero j
            if lista[j] < lista[smallest]: #si el valor de la posicion j en menor que el valor de la posicion del menor valor
                smallest = j #actualizamos el valor del valor mas pequeño de la lista
        lista[smallest], lista[i] = lista[i], lista[smallest]   #ordenar primero los valores mas pequeños
        
    print(lista)

listaZeros = [0,1,0,1,1,0,0,1,1,1,0]

def moverZeros(lista):
    posZero = 0
    for i in range(len(lista)):
        if lista[i] != 0:
            lista[posZero], lista[i] = lista[i], lista[posZero]
            posZero+=1
    return lista

listaSort = [0,1,2,1,2,1,2,1,0,2]
def sortNumeros(lista):
    left, rigth = 0, len(lista)-1
    i = 0
    while i < rigth:
        if lista[i] == 0:
            lista[left], lista[i] = lista[i], lista[left]
            left +=1
            i +=1
        elif lista[i] == 2:
            lista[rigth], lista[i] = lista[i], lista[rigth]
            rigth -=1
        else:
            i+=1
    return lista


listaSelect = [1,4,5,6,2,3,4,1,3,4,0]
def selectSort(lista):
    for i in range(len(lista) - 1):
        smallest = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[smallest]:
                smallest = j
    
        lista[i], lista[smallest] = lista[smallest], lista[i]
    return lista

def ordenacionInsercion(lista):
    pass
print("select sort")
print(selectSort(listaSelect))
print(sortNumeros(listaSort))
print(moverZeros(listaZeros))
ordenarNumeros(lista)