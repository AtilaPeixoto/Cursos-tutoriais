nome = input("digite nome ")
print("olaa! satisfaçao {:=^20} ".format(nome))
# seliga nisso dentro das chaves
# os dois pontos dizem quantos espaços sao disponibilizados para as chavez
#outros sinais como o de igual so apareceram com o comando de alinhamento
# o sinal de maior e menor poem a string a direita ou esquerda
# o acento circunflexo poem centralizado
print(nome*2)
print("="*20)
# perceba a nescessidade de aspas para efetiva multiplicaçao no caso de um nao objeto
n    = int(input("digite um numero:"))
n2   = int(input("digite o segundo numero:"))
s    = n + n2
su   = n - n2
d    = n / n2
di   = n // n2
po   = n ** n2
rd   = n % n2
print("A soma é {},\n a subtraçao é {}, a divisao é {},\n a divisao inteira é {}, a potencia é {}".format(s, su, d, di, po), end=" ")
# o  -> end=  <- no final junta os print's
# pr quebrar a linha o ->  \n  <-
print("o resto da div é {}".format(rd))

#=========exercicios
#  mostre um numero int e mostre na tea seu antecessor e sucessor
a = int(input("digite um numero"))
an = a - 1
su = a + 1
print("o numero antecessor é {}, o sucessor é {}".format(an, su))
print()
# crie um algoritimo que mostre o dorbro de um numero sua metade e sua raizQ
dobro = a *2
metade = a/2
raizQ = a**(1/2)
print("o dobro do numero é {}, a metade e {}, a raizQ é {}".format(dobro, metade, raizQ))

# programa que crie media
media = (n +n2 + a)/3
print(" a media entre os tres numeros digitados é {}".format(media))
print()
# programa que escreva a metragem e converta em centimetros e milimetros
cm = a *100
mm = cm *100
print(" se {} for em metros sua medida em milimetros e em centimetros seria de: {} cm, e {} mm".format(a, cm, mm))
print()
# faca um programa que vc digite um numero e entao revele-se a sua tabuada
print(" {} x {} = {}".format(a, 1, (a*1)))
print(" {} x {} = {}".format(a, 2, (a*2)))
print(" {} x {} = {}".format(a, 3, (a*3)))
print(" {} x {} = {}".format(a, 4, (a*4)))
print(" {} x {} = {}".format(a, 5, (a*5)))
print(" {} x {} = {}".format(a, 6, (a*6)))
print(" {} x {} = {}".format(a, 7, (a*7)))
print(" {} x {} = {}".format(a, 8, (a*8)))

# crie um algoritimo que calcule a area de uma parede e quantos litros de tinta preciso para pinta-la, sendo que cada litro pinta 2m
ap = float(input("qual altura da parede?"))
lp = float(input("Qual a largura da parede?"))
arep = ap * lp
baldes = arep /2
print("o total de baldes de tinta para a pintura da parede de area {}, será de {}".format(arep, baldes))
print()
# algorito que que calcule o preço de um item com um determinado desconto (5%)
desc = int(input(" caso o numero {} seja o valor de um produto, digite o desconto: ".format(a)))
nv = a - (a * (desc/100))
print(" o novo valor do item entao seria de {}".format(nv))
print()
# faca um algorimo que leia o slario de um funcionario e mostre um determinado aumento (15%)
salario = int(input("escreva o salario "))
acre    = int(input("Qual a porcentagem de aumento?"))
porcem = salario *(acre/100)
nsalario = salario + porcem
print("o novo salario é de, R${} ".format(nsalario))
print()
dias = float(input("quantos dias o cliente ficou com o carro?"))
km = float(input("Quantos km foram rodados?"))
vkm = km *0.15
vdias = dias * 60
vt = vkm +vdias
print("o valor do aluguem ficou em R${}".format(vt))