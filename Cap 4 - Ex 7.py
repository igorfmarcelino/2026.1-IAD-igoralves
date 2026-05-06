print("Este programa retorna a Nota de acordo com a pontuação fornecida, inserir um valor entre 0.0 e 1.0, qualquer valor diferente será considerado inválido\n\n")
def computarNotas(pont):
    if (pont>1.0 or pont<0.0):
        return("Pontuação Inválida")
    else:
        if (pont>=0.9):
            return("A")
        elif (pont>=0.8):
            return("B")
        elif (pont>=0.7):
            return("C")
        elif (pont>=0.6):
            return("D")
        elif (pont<0.6):
            return("E")

try:
    pontuacao = float(input("Digite a Pontuação: "))
    printPont = computarNotas(pontuacao)
    print (printPont)
except:
    print("Pontuação Inválida")