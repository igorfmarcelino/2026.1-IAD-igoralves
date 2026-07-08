cont = 0
numCtrl=0
while True:
    try:
        arquivo = input("Digite o nome de um arquivo: ")
        arq = open(arquivo)
        for linha in arq:
            if linha.startswith("X-DSPAM-Confidence:"):
                num = float(linha[linha.find(":")+1 :])
                cont += 1
                numCtrl += num
        print("Média de confiança de spam: "+str(numCtrl/cont))
        break
    except:
        print("\nNome de arquivo inválido, tente novamente.\n")
