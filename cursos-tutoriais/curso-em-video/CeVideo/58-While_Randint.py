from random import randint


cor = {"verde": "\033[32m",
       'branco': "\033[7m",
       'limpa':'\033[m'}


jogador = 0
genio = randint(1, 11)


while jogador != genio:
     jogador = int(input("Numero da SORTE: "))
     
     if jogador != genio:
         print(f'{cor["verde"]} Tente outa vez! {cor["limpa"]}')
     else:
         print(f'{cor["branco"]}Parabens, Acertou{cor["limpa"]}\nEscoli: {cor["branco"]}{genio}{cor["limpa"]}!!!')

