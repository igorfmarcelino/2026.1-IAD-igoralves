nome = input("Digite o nome do arquivo: ")
fhand = open(nome)

cont = 0

for linha in fhand:
    palavras = linha.split()

    if len(palavras) == 0:
        continue

    if palavras[0] != "From":
        continue

    print(palavras[1])
    cont = cont + 1

print("Há", cont, "linhas no arquivo com From como primeira palavra.")