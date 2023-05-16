import random
from time import sleep


jogo = []
limpa = []
numero = 0

numero_jogos = int(input('quantos jogos?'))


for i in range(0, numero_jogos):

    while len(limpa) != 6:
        numero = random.randint(1, 60)

        if numero not in limpa:
            limpa.append(numero)

    jogo.append(limpa[:])
    limpa.clear()


for indice, valor in enumerate(jogo):
    sleep(1)
    print(f'jogo {indice+1} : {valor}')




