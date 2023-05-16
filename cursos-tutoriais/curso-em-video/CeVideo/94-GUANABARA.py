


pessoa = dict()
galera = []
soma = 0

while True:
    pessoa['Nome'] = str(input('Nome: ').upper())
    
    while True:
        pessoa['Sexo'] = str(input('Sexo: ').upper()[0])
        
        if pessoa['Sexo'] in 'MF':
            break
        
        print('ERRO! igite valor valido')
        
        
    pessoa['Idade'] = int(input('Idade: '))
    soma += pessoa['Idade']
    galera.append(pessoa.copy())
    
    while True:
        f = str(input('Continuar[s/n]'))
        
        if f in 'sn':
            break
        print('Valor invalido digite [s/n]')
        
        
    if f == 'n':
        break
    

media = soma / len(galera)
print(f'Total de pessoas cadastradas {len(galera)}')
print(f'Media das pessoas cadastradas {media:2.2f}')
print(f'As mulheres cadastradas foram ', end=' ')


for p in galera:
    if p['Sexo'] in 'fF':
        print(f"{p['Nome']} ", end='')
        print()
        
print(f'As pessoas cadastradas acom idade acima da media são:')

for p in galera:
    
    if p['Idade'] >= media:
        print('  ', end='')
        
        for k, v in p.items():
            print(f'{k} = {v}; ', end=' ')
        print()
print('Encerrado')
