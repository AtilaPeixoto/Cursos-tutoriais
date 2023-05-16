d = float(input("Qual distancia a viagem "))
if d<=200:
    valor = d * 0.5
    print("O valor da passagem é {:.2f}".format(valor))
else:
    valor = d * 0.45
    print("o valor da passagem é {:.2f}".format(valor))