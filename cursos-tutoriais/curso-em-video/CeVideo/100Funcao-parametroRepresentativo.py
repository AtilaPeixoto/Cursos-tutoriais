import random
a = list()
pares = list()
c = list()


def escolha(e):
    while True:
        b = random.choice(e)
        if b not in c:
            c.append(b)
            if len(c) == 5:
                break
    return c

# verifica pares
def par(p):
    global pares
    for i in p:
        if i % 2 == 0:
            pares.append(i)
    if len(pares) > 0:
        return pares

# programa principal
while True:
    i = random.randint(0, 10)
    if i not in a:
        a.append(i)
        if len(a) >= 10:
            break

print(a)
escolha(a)
print(c)
par(c)
print(sum(pares))
