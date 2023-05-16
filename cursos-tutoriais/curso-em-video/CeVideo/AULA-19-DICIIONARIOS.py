estados = dict()
brasil = list()
for c in range(0, 3):
    estados['uf'] = str(input(' Unidade federativa'))
    estados['sigla'] = str(input('sigla'))
    brasil.append(estados.copy())
for e in brasil:
    for v in e.values():
        print(v, end=" ")
    print()

#for k, v in pessoas.items():
 #   print(f'{k} = {v}')