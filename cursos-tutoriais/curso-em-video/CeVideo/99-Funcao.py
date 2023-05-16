lista = []


def d():
    mx = max(lista)
    mn = min(lista)
    print(f'o maior numero add foi {mx}')
    print(f'o menor numero add foi {mn}')


while True:
    a = int(input('NUMERO: '))
    if a == 0:
        break
    
    lista.append(a)
    
    
print(f'Foram add {len(lista)}')

if len(lista) > 0:
    d()
else:
    print(f'Nenhum parametro foi add..')
