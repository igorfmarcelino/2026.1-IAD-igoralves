while True:
    try:
        nomeArq = input("Digite o nome do arquivo: ")
        fhand = open(nomeArq)

        emails = {}

        for linha in fhand:
            if not linha.startswith("From "): continue

            email = linha.split()[1]
            if email not in emails:
                emails[email] = 1
            else:
                emails[email]= emails[email]+1
        listaEmails = []
        for chave, valor in list(emails.items()):
            listaEmails.append((valor,chave))
        listaEmails.sort(reverse=True)
        print(listaEmails[0][1],listaEmails[0][0])
        break
    except:
      print("Arquivo inválido, tente novamente.\n")