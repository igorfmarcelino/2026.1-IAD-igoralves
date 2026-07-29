while True:
    try:
        nomeArq = input("Digite o nome do arquivo: ")
        fhand = open(nomeArq, encoding="utf-8")

        contaLetras = {}
        cont = 0
        lista=[]
        for linha in fhand:
            minusc = linha.lower()
            lista = minusc.split()
            while cont < len(lista):
                for letra in lista[cont]:
                    if letra.isalpha() is False: continue
                    else:
                        if letra not in contaLetras:
                            contaLetras[letra] = 1
                        else:
                            contaLetras[letra] += 1
                cont += 1
            cont = 0
        listaLetras=[]
        for chave,valor in list(contaLetras.items()):
            listaLetras.append((valor,chave))
        listaLetras.sort(reverse=True)
        for contagem in listaLetras:
            print(contagem[1],contagem[0])
        break
    except:
        print("Arquivo inválido, tente novamente")

            
                    

