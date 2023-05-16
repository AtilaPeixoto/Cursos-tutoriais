n = int(input("Digite um numero de 0 a 9999 "))
'''
# string
x = len(n)
n1 = " ".join(n)
n2 = n1.split(maxsplit=x)
print(n2)
print("""Unidade: {} 
Dezena: {}
Centena: {}
Milhar: {}""".format(n2[3], n2[2], n2[1], n2[0]))
# vai dar erro se menor que 4 digitos
'''
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print("""Unidade: {} 
Dezena: {}
Centena: {}
Milhar: {}""".format(u, d, c, m))
