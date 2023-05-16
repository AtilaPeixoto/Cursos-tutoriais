from random import randint


def fatorial(c):
    """
calcula fatorial
    :param c: minha versao
    :return: retornar o valor
    """
#   for i in range(1, c):
    f = 1
    for i in range(c, 0, -1):
        f *= i
       # print(c, end=" ")
    print()
    return f


a = randint(1, 5)
#print(f'fatorial de {a} é {fatorial(a)}')
help(fatorial)



