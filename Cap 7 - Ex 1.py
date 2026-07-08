while True:
    try:
        arquivo = input("Digite o nome de um arquivo: ")
        arq = open(arquivo)
        for linha in arq:
            print (linha.upper())
        break
    except:
        print("\nNome de arquivo inválido, tente novamente.\n")
