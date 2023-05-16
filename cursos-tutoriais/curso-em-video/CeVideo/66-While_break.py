


cont = soma = 0



while True:
    
    numero = int(input("digite um numero:"))
    
    if numero == 999:
        break
    
    soma += numero
    cont += 1
    
print(f"foram digitados {cont}e a soma entre eles é {soma}")
