from random import randint
itens = ("PEDRA", "TESOURA", "PAPEL")
pc = randint(0, 2)# NUMEROS
print("--=--"*20)
print("""Escolha um opção
[1] PEDRA
[2] TESOURA
[3] PAPEL
""")
jogador = int(input("Qual sua jogada? "))
print("-*-"*20)
print("O jogador jogou: {}".format(itens[jogador]))# LISTA
print("O PC jogou : {}".format(itens[pc]))

if pc == 1:
    if jogador == 1:
        print("EMPATE")
    elif jogador == 2:
        print("PC VENCE")
    elif jogador == 3:
        print("JOGADOR VENCE")
    else:
        print("JOGADA INVALIDA")
elif pc == 2:
    if jogador == 1:
        print("JOGADOR VENCE")
    elif jogador == 2:
        print("EMPATE")
    elif jogador == 3:
        print("PC VENCE")
    else:
        print("JOGADA INVALIDA")
elif pc == 3:
    if jogador == 1:
        print("PC VENE")
    elif jogador == 2:
        print("JOGADOR VENCE")
    elif jogador == 3:
        print("EMPATE")
    else:
        print("JOGADA INVALIDA")