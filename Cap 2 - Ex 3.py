print("Este programa calcula o valor a ser pago por um serviço. \n \nO usuário deverá fornecer a quantidade de horas trabalhadas e o valor da taxa por hora. \n \nVamos lá?")
horas = float(input("\nDigite as horas: "))
taxa = float(input("Digite a taxa: "))
print("Valor a ser pago: "+str(round(horas*taxa, 2)))