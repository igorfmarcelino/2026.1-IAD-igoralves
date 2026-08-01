import urllib.request

try:
    url = input("Digite a URL: ")

    arquivo = urllib.request.urlopen(url)

    mostrados = 0
    total = 0

    while True:
        data = arquivo.read(512)
        if len(data) == 0:
            break

        texto = data.decode()
        total += len(texto)

        if mostrados < 3000:
            restante = 3000 - mostrados
            print(texto[:restante], end="")
            mostrados += len(texto[:restante])

    print("\n\nTotal de caracteres recebidos:", total)

except:
    print("Erro: URL inválida ou documento não encontrado.")