import socket

try:

    url = input("Digite a URL: ")

    if url.startswith("http://"):
        url = url[7:]
    elif url.startswith("https://"):
        print("Este programa suporta apenas HTTP.")
        exit()

    partes = url.split("/", 1)
    host = partes[0]

    if len(partes) > 1:
        caminho = "/" + partes[1]
    else:
        caminho = "/"


    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))

  
    cmd = f"GET {caminho} HTTP/1.0\r\nHost: {host}\r\n\r\n"
    mysock.send(cmd.encode())

    mostrados = 0
    total = 0

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break

        texto = data.decode()
        total += len(texto)


        if mostrados < 3000:
            restante = 3000 - mostrados
            print(texto[:restante], end="")
            mostrados += len(texto[:restante])

    mysock.close()

    print("\n\nTotal de caracteres recebidos:", total)


except:
    print("Erro: URL inválida ou falha na conexão.")