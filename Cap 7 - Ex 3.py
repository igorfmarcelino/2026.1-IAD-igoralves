cont = 0
while True:
    try:
        arquivo = input("Digite o nome de um arquivo: ")
        if arquivo == "na na boo boo":
            print ("NA NA BOO BOO PRA VOCÊ TAMBÉM!\n")
        else:
            arq = open(arquivo)
            for linha in arq:
                if linha.startswith("Subject"):
                    cont += 1
            print("Há "+str(cont)+" linhas de assunto em: "+arquivo)
        break
    except:
        print("\nArquivo não pôde ser aberto: "+arquivo+". Tente novamente.\n")
