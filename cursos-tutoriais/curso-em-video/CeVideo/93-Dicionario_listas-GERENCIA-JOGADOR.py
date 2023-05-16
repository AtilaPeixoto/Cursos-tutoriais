jogador = {}
gols = {}
ficha = []
gol = []
ind = []
chave = {'NUMERO': 'OPÇAO', 'NOME': 'NOME', 'TOTAL DE GOLS': 'TOTAL GOLS'}
numero_jogadores = int(input('Quantos jogadores: '))


for nj in range(0, numero_jogadores):
    gol.clear()
    print('-=' * 20)
    jogador['Nome'] = str(input('Nome: ').upper())
    jogador['partidas'] = int(input('Numero de partidas: '))
    
    if jogador['partidas'] <= 0:
        jogador["gols"] = [0]
        jogador['MediaG'] = 0
        jogador['Gtotal'] = 0
        
    for i in range(0, jogador['partidas']):
        gol.append(int(input(f'Na partida {i + 1} foram gols: ')))
        jogador['gols'] = gol[:]
        jogador['Gtotal'] = sum(gol)
        jogador['MediaG'] = jogador['Gtotal'] / len(gol)
        
    ficha.append(jogador.copy())
    print(ficha)
    print()
    
while True:
    ind.clear()
    
    for i in chave.keys():
        print(f'{i:<10}', end='')
    print()
    
    for k, v in enumerate(ficha):
        print(f'[{k + 1:^5}]', end=' ')
        print(f"{v.setdefault('Nome'):^10}", end=' ')
        print(f"{v.setdefault('Gtotal'):^10}")
    a = str(input('Ver jogador individualmente? '))
    
    if a in "n":
        break
    else:
        b = int(input('DIGITE O NUMERO DO JOGADOR: '))
        b -= 1
        
        if b >= len(ficha):
            print('valor invalido.')
        else:
            ind.append(ficha[b])
            
    for x in ind:
        for z, c in x.items():
            print(f'\033[1m{z:<10} :{c}\033[m')
    print()
