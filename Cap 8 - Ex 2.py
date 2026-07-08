fhand = open('cap8ex2.txt')

for linha in fhand:
    palavras = linha.split()

    if len(palavras) == 0: continue

    if palavras[0] != 'De': continue

    if len(palavras) < 3: continue

    print(palavras[2])