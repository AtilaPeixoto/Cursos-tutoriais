from datetime import date




data = date.today()
ano_atual = data.year
cont_mulheres_menores_20 = cont_mulheres = cont_homens = cont_menores_18 = idade_mais_velha =0

while True:
    pessoa = str(input("NOME: ")).strip()
    nascimento = int(input("ANO DE NASCIMENTO: "))
    sexo = str(input("Genero[M/F]: ")).upper()
    add = input("Add outro[S/N]: ")
    idade = ano_atual - nascimento
    
    
    if idade < 18:
        cont_menores_18 += 1
        
    if sexo == "F":
        
        if idade < 20:
            cont_mulheres_menores_20 += 1
        cont_mulheres += 1
        
        
    elif sexo == "M":
        cont_homens += 1
        
        if idade > idade_mais_velha:
            
            homem_mais_velho = pessoa
            idade_mais_velha = idade
            
            
    if add == "n":
        break
    
    
print(f"""
O total de mulheres é {cont_mulheres}
O total de mulhere abaixo de 20 anos é {cont_mulheres_menores_20}
O total de homens é {cont_homens}
O homem mais velho é {homem_mais_velho}
O total de pessoas abaixo de 18 anos é {cont_menores_18}""")