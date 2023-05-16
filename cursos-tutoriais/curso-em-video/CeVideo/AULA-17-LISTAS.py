n = [2, 9, 6, 7, 8]
n[2] = 3
n.append(9)
print(f'foi add o numero 9 em {n}')
n.sort()
n.sort(reverse =True)
n.insert(2, 5)              # posiçao - obj
print(f'add numero 5 na posiçao 2', n)
if 5 in n:
    n.remove(5)
else:
    print('nao encontrado')
print(f' retirado o 5', n)
n.pop()                 # remove o ultimo  obj da lista/ ou indice e obj nele
print(f'essa lista{n} tem {len(n)} elementos')# lembre-se de que o 0 é numero contado
#####################
lista = []
lista.append(7)
lista.append(5)
lista.append(8)
lista.append(3)
for cont in range(0, 1):
    lista.append(int(input('digite um valor')))
for v in lista:
    print(f' a lista é {lista}...', end="")

for c, v in enumerate(lista):
    print(f' na posiçao {c} esta o valor {v}', end=' ')
#######################3
a = [1, 8, 9, 6, 4]
#b = a     #nao faça assim. neste caso é criado uma ligaçao e toda alteraçao em um é feita no outro
# o correto é assim
b = a[:]    # entao criada copia para mexer tranquilo sem alterar a lista A
b[2] = 8   # entao alteraçao acontece apenas na b e nao na a como no primeiro exemplo desativado
print(f' a lista a é {a}')
print(f' a lista b é {b}')

