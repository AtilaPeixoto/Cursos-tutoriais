


matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


for i in range(0, 3):
    for c in range(0, 3):
        matriz[i][c] = int(input(f'numero {i}, {c}'))

print('=-='*20)

for i in range(0, 3):
    for c in range(0, 3):
        print(f'{matriz[i][c]:^6}', end=' ')
    print()
