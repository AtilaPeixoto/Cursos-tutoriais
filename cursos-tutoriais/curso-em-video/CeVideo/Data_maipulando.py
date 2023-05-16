import datetime


now = datetime.datetime.now()
anonow = int(now.year)


nasc = int(input("Qual o ano de nascimento? "))
idade = int(anonow - nasc)


if idade == 18:
    print("Esta na Hora de alistar-se")
elif idade <=17:
    dif = 18 - idade
    print("Faltam {} anos para o alistamento".format(dif))
else:
    idade >18
    dif = idade - 18
    print("O tempo de alistamento ja passou em {} anos".format(dif))