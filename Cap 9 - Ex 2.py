while True:
    try:
        nome = input("Digite o nome do arquivo: ")
        fhand = open(nome)

        dias = {}

        for linha in fhand:
            palavras = linha.split()

            if len(palavras) == 0:
                continue

            if palavras[0] != "From":
                continue

            dia = palavras[2]

            if dia not in dias:
                dias[dia] = 1
            else:
                dias[dia] = dias[dia] + 1

        print(dias)
        break
    except:
        print("Arquivo inválido, tente novamente.")