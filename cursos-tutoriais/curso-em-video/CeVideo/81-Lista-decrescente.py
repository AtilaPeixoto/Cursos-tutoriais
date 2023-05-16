



minha_lista = []
lista_impares = []
lista_pares = []

minha_lista.append(int(input('add à lista')))

# questionando para adição de mais um numero
while 'sn' not in mais_um_numero:
    mais_um_numero = str(input('add outro').lower())

    if mais_um_numero == 's':
        minha_lista.append(int(input('add à lista')))
    elif mais_um_numero == "n":
        break
    else:
        print('valor invalido digite [s/n]')


# organizando de tras para frente/ decrescentemente
minha_lista.sort(reverse=True)
print(f'ordem decrescente', minha_lista)


# organizando na ordem crescente
minha_lista.sort()
print(f' ordem crescente', minha_lista)

print(f' usando fçao para somar à lista', sum(minha_lista))



# trocando de lista/ discriminando
for i in range(0, len(minha_lista)):

    if minha_lista[i] % 2 == 0:
        lista_impares.append(minha_lista[i])
    else:
        lista_pares.append(minha_lista[i])


print(f'lista com impares de lista A', lista_pares)
print(f' lista com pares de lista A', lista_impares)
print(f'lista A', minha_lista)
