def corte(lista):
    del lista[0]
    del lista[-1]
    return None

def meio(lista):
    return lista[1:-1]

numeros = [1, 4, 5, 9, 14]

print("Lista original:", numeros)

novaLista = meio(numeros)
print("Resultado de meio():", novaLista)
print("Lista original após meio():", numeros)

corte(numeros)
print("Lista após corte():", numeros)