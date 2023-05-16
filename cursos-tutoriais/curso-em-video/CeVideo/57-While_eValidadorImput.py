


contMasculino = 0
contFeminino = 0
fim = " "


while fim not in "n":
    genero = str(input(" Para Masculino [M] para Feminino [F]")).strip().upper()
    print(genero)
    
    # caracteristica importante "not in " ao inves de != para verificaçao
    if genero not in "MF":
        print(f"Valor invalido")
        
    elif genero == "F":
        contFeminino += 1
        
    elif genero == "M":
        contMasculino += 1

    print("-=-" * 40)
    fim = str(input("Add outro?[S/N] :")).lower()
    
    
print("=="*20)
print(f"O total de  Homens é {contMasculino} \nO total  mulheres é {contFeminino}")
