



lista_pares = []
lista_impares = []
lista = []

for cada in range(0, 5):
    numero = int(input('numero'))
    
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)
        
        
lista_pares.sort()            
lista_impares.sort()
# lembre de add os dois pontos para que toda a lista seja add a nova lista
lista.append(lista_pares[:])
lista.append(lista_impares[:])
print(lista)