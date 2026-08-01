import socket

try:
    url = input("Digite a URL: ")

    if url.startswith("http://"):
        url = url[7:]

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

    cabecalho_encontrado = False
    buffer = b""

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break

        if not cabecalho_encontrado:
            buffer += data

            indice = buffer.find(b"\r\n\r\n")

            if indice != -1:
                cabecalho_encontrado = True

                
                corpo = buffer[indice + 4:]
                print(corpo.decode(), end="")
        else:
            print(data.decode(), end="")

    mysock.close()

except:
    print("Erro ao acessar a página.")