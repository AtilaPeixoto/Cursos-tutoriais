from random import randint



numero_escolha_usuario = int(input('numero a ser encontrado'))

numeros_aleatorios_lista = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print(numeros_aleatorios_lista)
print(f"o numero 9 apareceu {numeros_aleatorios_lista.count(9)}")
print(f'o menor valor {min(numeros_aleatorios_lista)}')
print(f'o maior vaor {max(numeros_aleatorios_lista)}')
if numero_escolha_usuario in numeros_aleatorios_lista:
    # lembresse de que o zero é a primeira posicao. Digo um numero valido
    print(f'ha um {numero_escolha_usuario} na posiçao', numeros_aleatorios_lista.index(numero_escolha_usuario))
else:
    print('numero nao esta presente')
