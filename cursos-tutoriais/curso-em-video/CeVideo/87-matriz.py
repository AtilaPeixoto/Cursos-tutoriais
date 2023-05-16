


matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_par = soma_coluna_3 = maior_valor_dos_pares = 0


for i in range(0, 3):
    for c in range(0, 3):
        matriz[i][c] = int(input(f'numero {i}, {c}'))

print('=-='*20)
for i in range(0, 3):
    for c in range(0, 3):
        print(f'{matriz[i][c]:^6}', end=' ')
        if matriz[i][c] % 2 == 0:
            soma_par += matriz[i][c]
    print()


for i in range(0, 3):
    soma_coluna_3 += matriz[i][2]

for c in range(0, 3):
    if matriz[1][c] > maior_valor_dos_pares:
        maior_valor_dos_pares = matriz[1][c]


print(f'a soma dos valores da 3 coluna é {soma_coluna_3}')
print(f'o maior elemento da segunda linha é {maior_valor_dos_pares}')
print(f' a soma dos numeros pares é {soma_par}')