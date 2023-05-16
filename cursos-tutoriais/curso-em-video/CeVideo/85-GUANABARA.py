


lista = [[], []]   # tres listas

for x in range(0, 5):
    n = int(input('numero'))
    
    if n % 2 == 0:
        lista[0].append(n)    # pares
    else:
        lista[1].append(n)  # impares
        
        
        
lista[0].sort()            # o .sort precisa ser feito aparte para cada lista/sbulista
lista[1].sort()
print(lista)
