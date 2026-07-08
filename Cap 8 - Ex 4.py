palavras = []

fhand = open('romeo.txt')

for linha in fhand:
    lista = linha.split()

    for palavra in lista:
        if palavra not in palavras:
            palavras.append(palavra)

palavras.sort()

print(palavras)