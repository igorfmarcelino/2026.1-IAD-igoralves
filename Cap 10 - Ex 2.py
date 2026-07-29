while True:
    try:
        nomeArq = input("Digite o nome do arquivo: ")
        fhand = open(nomeArq)

        horas = {}
        for linha in fhand:
            if not linha.startswith("From "): continue

            horaCompleta = linha.split()[5]
            hora = horaCompleta.split(':')[0]
        
            if hora not in horas:
                horas[hora] = 1
            else:
                horas[hora] += 1
        listaHoras = []

        for chave, valor in list(horas.items()):
            listaHoras.append((chave,valor))
            listaHoras.sort()
        for hora in listaHoras:
            print (hora[0],hora[1])
        break
    except:
        print("Arquivo inválido, tente novamente.\n")
