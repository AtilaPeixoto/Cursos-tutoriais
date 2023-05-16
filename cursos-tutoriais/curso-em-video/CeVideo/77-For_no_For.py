



lista_palavras = 'palavra', 'mesa', 'cafe', 'video', 'celular'

for palavra in lista_palavras:
    print(f'\nNa palavra "{palavra}" temos :', end='')
    
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end='')