print("Este programa converte uma temperatura fornecida em Celsius (°C) para a escala Fahrenheit (°F).\n")
tempCelsius = float(input("Digite a temperatura em Celsius: "))
tempFarenheit = round(float((tempCelsius*(9/5))+32),1)
print("\nA temperatura "+ str(tempCelsius)+" °C convertida para Fahrenheit é de: "+str(tempFarenheit)+" °F.")