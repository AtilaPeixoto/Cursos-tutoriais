ficha = []
jogador = {}


def fic(an="", ag=''):  # a str vazia estava retornando vazia
    """
    veifica se a nome e gols do jogador e os add em dicionario
    :param an: nome do jogador
    :param ag: gols do jogaor
    :return: retorna dicionario
    """

    if ag.isnumeric():
        ag = int(ag)
    else:
        ag = 0
        
    if an == '':        # foi preciso para que nao voltasse vazia
        an = 'DESCONHECIDO'
    jogador['NOME'] = an
    jogador['GOLS'] = int(ag)
    print(jogador)
    return jogador


while True:
    a = str(input('NOME:    '))
    b = str(input('GOLS:    '))
    
    print(fic(a, b))
    
    ficha.append(jogador.copy())
    fim = str(input('\033[7mADD OUTRO?[S/N]\033[m')).lower()
    
    if 'n' in fim:
        break
    
print(ficha)

for i in jogador.keys():
    print(f'\033[1m{i:<9}\033[m', end=' ')
    
    
print()
for i in ficha:
    print('='*30)
    
    for k, v in i.items():
        print(f'{k:<5}: {v:^10}'.upper())
