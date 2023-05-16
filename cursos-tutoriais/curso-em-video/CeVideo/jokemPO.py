import random
from time import sleep
print("JokemPO Esolha um!!!")
jogo = int(input("""
[1]PEDRA
[2]PAPEL
[3]TESOURA
Sua escolha: 
"""))### se nao dizer que é numero, nao funcionou. é preciso dizer que é numero!
lista = ["PEDRA", "PAPEL", "TESOURA"]
# o codigo do guanabara consegui transformar em numero o  randomico
escolha = random.randint(0, 2)

if escolha == 1 and jogo == 0:
    v = " PC venci!!!"
elif escolha == 2 and jogo == 0:
    v = " Voce venceu!!!"
elif escolha == 0 and jogo == 1:
    v = " Voce venceu!!!"
elif escolha == 2 and jogo == 1:
    v = " PC venci!!!"
elif escolha == 0 and jogo == 2:
    v = "PC VENCEU!!!"
elif escolha == 1 and jogo == 2:
    v = " Voce venceu!!!"
else:
    v = "EMPATE"


print("-=-"*20)
print("             JO")
sleep(1)
print("             KEN")
sleep(1)
print("             PO")
sleep(1)
print("-=-"*20)
print("O jogador jogou: {}".format(lista[jogo]))# LISTA
print("O PC jogou : {}".format(lista[escolha]))
print("{}{}{}".format('\033[7m', v, '\033[m'))
print("-=-"*20)
# quando cor dentro do format é preciso usar chave para abrir cor e outra par fechar, totalizando tres chaves.