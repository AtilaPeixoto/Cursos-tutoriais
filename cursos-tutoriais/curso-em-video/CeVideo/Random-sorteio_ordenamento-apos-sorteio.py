import math
import random


exe = "exercicio"
'''
print("{:=^20}".format(exe))
are = float(input("numero a ser  reondado"))
aredo = math.trunc(are)
print(aredo)
print()

print("{:=^20}".format(exe))
n = int(input("digite um numero "))
raiz = math.sqrt(n)
print("a raiz de {} e´igual a {:.2f} ".format(n, raiz))
# o ponto e o numero de casas ecimais dentro do format
# a biblioteca random gera numeros aleatorios menores que 1 e maiores que 0 ranom.randomint(x, y)gera inteiros de ate.

print("{:=^20}".format(exe))
co= float(input("cateto oposto "))
ca = float(input("cteto adjacente "))
hipo = math.hypot(co, ca)
print("o valor da hipotenusa é {:.5f}".format(hipo))
print()

print("{:=^20}".format(exe))
angulo = float(input("qual angulo? "))
#graus graus radianos, outros numeros normais.
cos = math.cos(math.radians(angulo))
sen = math.sin(math.radians(angulo))
hipotenusa = math.tan(math.radian(angulo))
print("o valor de coseno é {}, \ne o valor de seno é {}, \n e o valor da tangente é{}".format(cos, sen, hipotenusa))
print(
    '''
print("{:=^20}".format(exe))
a1 = "joao"
a2 = "guilherme"
a3 = "magnus"
a4 = "tito"
lista = [a1, a2, a3, a4]
escolido = random.choice(lista)
print(" O ESCOLIDO FOI \n*********", escolido,"**********")
#fazer com que apareça a ordem de sorteio
random.shuffle(lista)
#o metodo shuffle embaralha o objeto, en.entoa nao é possivel atriuir uma variavel para ele exlusivamente, sim eu tentei.
print("a ordem para apresentçao do trabaho é")
print(lista)