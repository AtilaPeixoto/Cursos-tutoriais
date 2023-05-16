ficha = []
while True:
    nome = str(input('nome:'))
    nota1 = float(input('nota '))
    nota2 = float(input('nota '))
    media = (nota1 + nota2) /2
    ficha.append([nome, [nota1, nota2], media])
    r = str(input(' parar:').lower())
    if r == "n":
        break
       # etc....
