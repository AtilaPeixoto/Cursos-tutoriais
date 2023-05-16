



minha_tupla = (int(input("digite um numero: ")),
     int(input("digite um numero: ")),
    int(input("digite um numero: ")),
    int(input("digite um numero: ")))

print(f'voce dgitou os valores {minha_tupla}')
print(f'o volar 9 apareceu {minha_tupla.count(9)} vezes')

if 3 in minha_tupla:
    print(f'o valor 3 apareceu na posiçao {minha_tupla.index(3)}')
else:
    print('o valor 3 nao esta presente')