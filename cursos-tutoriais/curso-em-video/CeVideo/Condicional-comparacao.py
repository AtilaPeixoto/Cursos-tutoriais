


n = int(input("escreva o primeiro numero "))
n2 = int(input("escreva o segundo numero "))



iguais = "nao existe maior. eles sao iguais"

if n == n2:
    print(iguais)
elif n > n2:
    print("O primeiro valor é o maior. \nO segundo valor é o menor")
else:
    print("O Segundo valor é maior. \nO primeiro valor é menor.")