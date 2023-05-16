



ano = int(input("Digite o ano para saber se é bissesxto "))

if  ano % 4 == 0 and ano % 100 != 0  or ano % 400 == 0:
     print("O ano é bissesto")
else:
   print("ano normal")
   print()


print(" {:=^20}".format("outro exercicio"))


n = int(input("Você digitará 3 numeros.\n digite o primeiro"))
n2 = int(input("digite o segundo "))
n3 = int(input(" digite o terceiro "))

if n > n2:
    maior = n
elif n3 > n2:
    maior = n3
else:
    maior = n2

if n < n2:
    menor = n
elif n3 < n2:
    menor = n3
else:
    menor = n2

if maior >= menor + n or maior >= menor + n2 or maior >= menor + n3:
    t = "Não formam umm triangulo"
else:
    t = "Formam um triangulo"

print(f" o maior numero digitado entre os tres foi {maior}\n e  menor é {menor}")
print(t)


