while True:
    try:
        nome = input("Digite o nome do arquivo: ")
        fhand = open(nome)

        palavras = {}

        for linha in fhand:
            lista = linha.split()

            for palavra in lista:
                palavras[palavra] = True

        busca = input("Digite uma palavra para procurar: ")

        if busca in palavras:
            print("A palavra '",busca,"' está no arquivo.")
        else:
            print("A palavra '",busca,"' não está no arquivo.")
        break
    except:
        print("Arquivo inválido, tente novamente.")