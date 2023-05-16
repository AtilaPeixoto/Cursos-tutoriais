

# progressao aritimetica

numero_inicial = int(input("Digite o numero inicial:    "))
razao = int (input("Digite a razao:    "))

cont = 0
cont_repeticao = -1
limite_numeros = 10


print(numero_inicial, end= " ")

while limite_numeros != 0:
        
    i = 0  
    while i != limite_numeros:
        numero_inicial += razao
        print(numero_inicial, end=" ")
        cont += 1
        i += 1
        
    print()
    cont_repeticao += 1
    aumentar_limite_numeros = int(input("quer ver mais quantos termos?    "))
    limite_numeros = aumentar_limite_numeros
    
    
print("-=-"*20)
print(f"foram revelados {cont} da PA solicitada.\nCom {cont_repeticao} repetiçoes extras")


