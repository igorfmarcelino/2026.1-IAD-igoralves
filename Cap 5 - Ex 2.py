acumul = 0
cont = 0
max = None
min = None
while True:
    numCtrl = input("Digite um número: ")
    if numCtrl == "pronto":
        break
    else:
        try:
            num = int(numCtrl)
            if max is None or num > max:
                max = num
            if min is None or num < min:
                min = num
            acumul = acumul + num
            cont = cont + 1
        except:
            print("Entrada Inválida")
print(acumul,cont,"Máximo:",max,"Mínimo:",min)