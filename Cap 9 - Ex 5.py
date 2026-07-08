while True:
    try:
        nome = input("Digite o nome do arquivo: ")
        fhand = open(nome)

        dominios = {}

        for linha in fhand:
            palavras = linha.split()

            if len(palavras) == 0:
                continue

            if palavras[0] != "From":
                continue

            email = palavras[1]
            dominio = email.split("@")[1]

            if dominio not in dominios:
                dominios[dominio] = 1
            else:
                dominios[dominio] = dominios[dominio] + 1

        print(dominios)
        break
    except:
        print("Arquivo inválido, tente novamente.")