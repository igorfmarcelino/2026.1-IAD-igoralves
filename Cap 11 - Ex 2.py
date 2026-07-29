import re
cont=0
rev=0
while True:
    try:
        nomeArq = input("Arquivo de entrada: ")
        fhand = open(nomeArq)

        for linha in fhand:
            linha = linha.rstrip()
            x = re.findall('New Revision: ([0-9]+)', linha)
            if len(x)>0:
                  rev += int(x[0])
                  cont += 1

        print(rev/cont)
        break
    except:
        print("Arquivo inválido, tente novamente.")