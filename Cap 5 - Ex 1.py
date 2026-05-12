acumul = 0
cont = 0
while True:
    numCtrl = input("Digite um número: ")
    if numCtrl == "pronto":
        break
    else:
        try:
            num = int(numCtrl)
            acumul = acumul + num
            cont = cont + 1
        except:
            print("Entrada Inválida")
print(acumul,cont,acumul/cont)