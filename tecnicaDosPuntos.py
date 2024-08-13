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

lista = [1,3,4,6,8,10,13]
print(encontrarSUMA(lista, 13))
print(encontrarSumaExtremos(lista, 13))