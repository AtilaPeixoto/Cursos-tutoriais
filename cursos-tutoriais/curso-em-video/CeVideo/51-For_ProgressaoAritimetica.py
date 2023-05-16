



inicio = int(input("Digite o numero inicial "))
razao = int(input("Digite a razao(salto) "))


decimo = inicio +(10 ) *razao

# calcular o decimo termo, para nao ser 10 mas decimo
for x in range(inicio, decimo, razao):
    print(x, end="->")
    
    
   
print("Fim")