from random import  randint
g = randint(1, 10)
acertou = False
palpites = 0
while not acertou:
    j = int(input("escolha um numero: "))
    palpites += 1
    if j == g:
        acertou = True
    else:
        if j < g:
            print("MAIS")
        elif j > g:
            print("MENOS")
print("Acertou com {} palpites!!! PARABENS!!!".format(palpites))