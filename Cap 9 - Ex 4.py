while True:
    try:
        nome = input("Digite o nome do arquivo: ")
        fhand = open(nome)

        emails = {}

        for linha in fhand:
            palavras = linha.split()

            if len(palavras) == 0:
                continue

            if palavras[0] != "From":
                continue

            email = palavras[1]

            if email not in emails:
                emails[email] = 1
            else:
                emails[email] = emails[email] + 1

        maiorEmail = None
        maiorQtd = None

        for email in emails:
            if maiorQtd is None or emails[email] > maiorQtd:
                maiorEmail = email
                maiorQtd = emails[email]

        print(maiorEmail, maiorQtd)
        break
    except:
        print("Arquivo inválido, tente novamente.")