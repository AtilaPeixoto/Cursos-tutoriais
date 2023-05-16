from datetime import date

agora = date.today()
ano = agora.year
ind = dict()

ind['Nome'] = str(input('Nome: ').strip().upper())
ano_nascimento = int(input('Ano de nascimento: '))
ind['Idade'] = int(ano - ano_nascimento)
ind['Ncarteira'] = int(input('Numero da carteira de trabalho: '))


if ind['Ncarteira'] > 0:
    ind['Tempo'] = int(input('Tempo trabalhando: '))
    
    if ind['Tempo'] != 0:
        ind['Salario'] = float(input('Salario: '))
        
else:
    ind['Tempo'] = 0
falta = 35 - ind['Tempo']


if falta <= 35:
   t = int(ind['Idade'] + falta)
else:
    t = 0
print('-='*20)


for i, c in ind.items():
    print(f'{i:<10}---{c:>10} ')
print(f'-- aposentadoria vira com : {t} ')
