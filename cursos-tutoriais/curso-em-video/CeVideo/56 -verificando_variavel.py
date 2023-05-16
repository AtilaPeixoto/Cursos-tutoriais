'''56 PROGRAMA QUE LEIA NOME IDADE E SEXO E 4 PESSOAS. NO FINAL  MOSTRE
- A MEDIA DE IDADE
- QUAL NOME DO HOMEN MAIS VELHO
- QUANTAS MULHERES TEM MENOS DE 20 ANOS'''


from datetime import date
data = date.today()
ano_atual = data.year

mulher_jovem = 0
soma_idade = 0
idade_homem_velho = 0
homem_velho = ""

arte = ("-----==----" * 5)
sexo = str(" " "Masculino" "Feminino")

for cada in range(1, 4):
    print(arte)
    
    nome = str(input("Nome "))
    nascimento = int(input("Nascimento   "))
    sexo = input("Sexo: [1] Masculino [2] Feminino   ").strip()
    
    idade = ano_atual - nascimento
    soma_idade += idade
    
    if cada == 1 and sexo == "1":
        homem_velho = nome
        idade_homem_velho = idade 
            
    if sexo in "1" and idade > idade_homem_velho:
        homem_velho = nome   
        idade_homem_velho = idade 
             
    if sexo in "2" and idade < 20:
        mulher_jovem += 1 
             
    print(arte)
    
media = soma_idade / 3 
      
print(arte)
print(f"""A media de idade é {media}
O nome do Homem mais velho é {homem_velho} com {idade_homem_velho} idade 
Mulheres abaixo dos 20 anos Totalizaram {mulher_jovem}
""")