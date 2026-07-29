import socket

while True:
    try:
        nomeUrl = input("Digite o nome da URL (exemplo: http://data.pr4e.org/): ")
        if nomeUrl.startswith("http://"):
            url = nomeUrl[7:]
        else:
            print("URL incorreta, tente novamente.")
            continue
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysock.connect((url, 80))
        cmd = 'GET '+url+' HTTP/1.0\r\n\r\n'
        mysock.send(cmd.encode())

        while True:
            data = mysock.recv(512)
            if len(data) < 1:
                break
            print(data.decode(),end='')

        mysock.close()
        break
    except:
        print("URL incorreta, tente novamente.")