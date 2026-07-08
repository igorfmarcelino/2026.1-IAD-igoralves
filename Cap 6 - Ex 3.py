def acharLetra(palavra, letra):
    contagem = 0
    for let in palavra:
        if let == letra:
            contagem = contagem + 1
    return(contagem)

palavra = input("Digite uma palavra: ")
letra = input("Digite a letra que gostaria de contar na palavra: ")
print ("O número total de letras '"+letra+"' é "+str(acharLetra(palavra, letra)))