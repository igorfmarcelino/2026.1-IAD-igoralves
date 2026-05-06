print("Este programa calcula o valor a ser pago por um serviço. \n \nO usuário deverá fornecer a quantidade de horas trabalhadas e o valor da taxa por hora. \n \nVamos lá?")

def calculoPagamento(horas, taxaHora):
    if horas <= 40:
        print("Valor a ser pago: "+str(round(horas*taxaHora, 2)))
    else:
        print("Valor a ser pago: "+str(round((40*taxaHora)+((horas-40)*taxaHora*1.5), 2)))
        
try:
    hrs = float(input("\nDigite as horas: "))
    txHrs = float(input("Digite a taxa: "))
    calculoPagamento(hrs, txHrs)
except:
    print("Erro, por favor utilize uma entrada numérica")