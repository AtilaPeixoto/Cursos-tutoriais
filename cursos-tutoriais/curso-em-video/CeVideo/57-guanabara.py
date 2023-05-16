cont = 0
while cont <4:
    sexo = str(input("informe seu sexo[M/F] ")).strip().upper()[0]
    print(sexo)
    while sexo not in "MF":
        sexo = str(input("invalido")).strip().upper()
    print("sexo registrado com sucesso")
cont+=1
