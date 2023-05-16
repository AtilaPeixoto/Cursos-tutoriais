p = float(input("Qual preço do produto? "))
print("Escolha a forma de pagamento")
forma = input("""[1] avista
[2] credito
[3] cretido ate 2x
[4] credito mais de 3x
              """)
if forma == 1:
    p = p - (p*(10/100))
    print("valor do produdo é R${}".format(p))
elif forma == 2:
    p = p - (p*(10/100))
    print("o valor do produto é R${}".format(p))
elif forma == 3:
    p = p
    print("o valor do produto é {}".format(p))
else:
    p = p +(p * (20/100))
    print("o valor do produto é {}".format(p))