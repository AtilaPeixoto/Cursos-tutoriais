







while True:
    
    numero = int(input("Você quer saber a dtaboada do numero: "))
    
    if numero <= 0:
        break
    
    for numero_em in range(1, 11):
        taboada = numero_em * numero
        print(f"[ {numero_em:^2}] X [{numero}] = {taboada}")
