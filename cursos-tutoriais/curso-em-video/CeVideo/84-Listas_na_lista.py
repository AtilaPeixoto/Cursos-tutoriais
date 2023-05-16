
pessoa = []
grupo = []
leves = []
pesados = []


while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    
    # os dois pontos sao excenciais para que o proximo comando afete apena a lista pessoa
    grupo.append(pessoa[:])
    # o resultado é uma lista de listas, em que cada lista tem nome e peso de uma pessoa             
    pessoa.clear()                  
    x = input('ad outro?')
    
    if x == 'n':
        break
    
    
for i in grupo:
    
    if i[1] >= 100:
        pesados.append(i[0])
    elif i[1] <= 65:
        leves.append(i[0])
        
print(f'\033[7mLISTA DOS ABAIXOS DOS 65Kg\033[m')

for i in leves:   
    print(i)
    
print(f'\033[7mLISTA DOS COM PESO ACIMA DOS 100Kg\033[m')
for i in pesados:
    print(i)


