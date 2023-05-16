


maior = 0
menor = 0


for i in range(1, 4):
    peso = int(input("Digite o peso: "))
    
    if i == 1:
       maior = peso
       menor = peso
    else:
        if peso < menor:
            menor = peso
        if peso > maior:
            maior = peso
            
print(f"O maior peso é {maior} \nO menor peso é {menor}")