numeros = []

while True:
    entrada = input("Digite um número: ")

    if entrada == "feito":
        break

    try:
        numero = float(entrada)
        numeros.append(numero)
    except:
        print("Entrada inválida.")

print("Máximo:", max(numeros))
print("Mínimo:", min(numeros))