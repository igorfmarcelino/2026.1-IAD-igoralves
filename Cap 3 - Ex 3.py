print("Este programa retorna a Nota de acordo com a pontuação fornecida, inserir um valor entre 0.0 e 1.0, qualquer valor diferente será considerado inválido\n\n")
try:
    pont = float(input("Digite a Pontuação: "))
    if (pont>1.0 or pont<0.0):
        print("Pontuação Inválida")
    else:
        if (pont>=0.9):
            print("A")
        elif (pont>=0.8):
            print("B")
        elif (pont>=0.7):
            print("C")
        elif (pont>=0.6):
            print("D")
        elif (pont<0.6):
            print("E")
except:
    print("Pontuação Inválida")