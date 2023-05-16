

minha_ista = []


for i in range(0, 4):
    numero = int(input('digite numero '))

    # se o indice for 0 ou caso o numero for maior que o numero na ultima posicao na lista
    if i == 0 or numero > minha_ista[-1]:
        minha_ista.append(numero)
    else:
        posicao = 0

        while posicao < len(minha_ista):

            if numero <= minha_ista[posicao]:
                minha_ista.insert(posicao, numero)
                break

            posicao += 1

print(minha_ista)
