from datetime import date

agora = date.today()
ano = agora.year
metrica = []
pessoas = []
mulheres = {}
homens = {}
velhos = {}
somaif = somaim = mediaf = mediam = 0
f = ''

while f != 'n':
    if len(velhos) > 0:
        velhos.clear()
    nome = str(input('NOME ').upper().strip())
    nasc = int(input('Ano de nascimento '))
    idade = ano - nasc
    sexo = str(input('SEXO ')[0].upper())
    
    if 'F' in sexo[0]:
        mulheres['nome'] = nome
        mulheres['idade'] = idade
        mulheres['sexo'] = sexo[0]
        pessoas.append(mulheres.copy())
        somaif += idade

        if len(mulheres) > 0:
            mediaf = somaif / len(mulheres)
        else:
            mediaf = 0

        if idade == mediaf:
            velhos = {nome: idade}

    else:
        homens['nome'] = nome
        homens['idade'] = idade
        homens['sexo'] = sexo[0]
        pessoas.append(homens.copy())
        somaim += idade

        if len(homens) > 0:
            mediam = somaim / len(homens)
        else:
            mediam = 0

        if idade > mediam:
            velhos = {nome: idade}


    metrica.append(velhos.copy())
    print('-='*20)
    f = str(input('\033[31mAdd outro\033[m'))
    print('-='*20)


print(f'''
total de homens {len(homens)}
media de idade dos homens {mediam}
total de mulheres {len(mulheres)}
media de idade das mulheres {mediaf}
''')

print('\033[7mPessoas com IDADE acima da media geral\33[m')

for i in metrica:
    for c, d in i.items():
        print(f'nome: {c} idade {d}')





