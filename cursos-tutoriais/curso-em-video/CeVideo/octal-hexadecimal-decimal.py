qt ="Escolha para qual tipo quer converte-lo"

print("{:=^40}".format("Convertendo numeros"))
n = int(input("Digite um numero par a conversão"))
tipo = int(input("""Escolha o formato em que sera convertido.
[1] binario
[2] hexadecimal
[3] octal
Sua opçao: """))
fim = "O resultado da conversão de {} é ".format(n)
if tipo == 1:
    r = bin(n)
    print("{} ".format(fim), '\033[7m', r[2:], '\033[m')
elif tipo == 2:
    r = hex(n)
    print("{} ".format(fim),"\033[7m", r[2:],'\033[m')
else:
    tipo == 3
    r = oct(n)
    print("{} ".format(fim), '\033[7m', r[2:], '\033[m')
