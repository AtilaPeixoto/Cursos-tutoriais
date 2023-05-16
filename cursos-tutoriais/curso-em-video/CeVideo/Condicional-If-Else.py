




s = float(input("Digite o salario do funcionario "))



if 1250 > s:
    porcem = s*(15/100)
    ns = s+ porcem
else:
    porcem = s*(10/100)
    ns = s + porcem



print("o novo salario será de {:.2f}".format(ns))