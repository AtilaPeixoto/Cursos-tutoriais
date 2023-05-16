



minha_lista = []

for itens in range(0, 5):
    minha_lista.append(int(input('digite um numero')))

print(minha_lista)
minimo_valor = min(minha_lista)
maximo_valor = max(minha_lista)


print(f'\nO maior é numero{maximo_valor}')
print(f'\nO menor  é numero{minimo_valor} ')
print()

for indice, valor in enumerate(minha_lista):
    print(indice, valor)
    if valor == minimo_valor:
       indice_menor = indice



for indice, valor in enumerate(minha_lista):
    if valor == maximo_valor:
        indice_maior = indice

print(f'\nA posição do menor é {indice_menor+1} no indice {indice_menor}')
print(f'\nA posiao do maior é `{indice_maior+1} no indice {indice_maior}')