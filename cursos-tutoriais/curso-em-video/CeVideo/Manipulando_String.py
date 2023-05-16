n0 = str(input("Qual seu nome completo "))
n = n0.lower()
n1 = n.split()
n2 = len(n)
n3 = len(n1)
n4 = n2 - n3 +1
print(n4)
# um contador conta a quantidade de nomes, outro a quantidade de letras.
# quando dois nome (minimo ) ha apenas um espaço, entao acrescido o primeiro nome novamente
# esta tecnica fuincionou para x nomes
n5 = len(n1[0])
print("A quantia de letras do primeiro nome é {}".format(n5))