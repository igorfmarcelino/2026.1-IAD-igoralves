import re
cont=0
fhand = open("mbox.txt")
grep = input("Digite uma expressão regular: ")
for linha in fhand:
    linha = linha.rstrip()
    if re.search(grep,linha):
        cont+=1


print ("mbox.txt teve",cont,"linhas que se igualam a", grep)