from time import sleep
from operator import itemgetter
import random


jogadores = ['marcelo', 'joao', 'marco', 'atila']
jogador = {}
jogo = []
nome = ''


for i in range(0, 4):
    nome = random.choice(jogadores)
    jogadores.remove(nome)
    jogador[nome] = random.randint(1, 6)
    
jogo.append(jogador.copy())
print(jogo)
ranking = list()


for i in jogo:
    for x, j in i.items():
        sleep(1)
        print(f'{x:<10} -> {j}'.upper())
        
        
ranking = sorted(jogador.items(), key=itemgetter(1), reverse=True)
print(ranking)

for i, v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]:<10} com {v[1]}'.upper())
    sleep(1)

