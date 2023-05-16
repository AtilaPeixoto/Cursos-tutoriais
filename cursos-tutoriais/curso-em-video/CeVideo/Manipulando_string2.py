nome = str(input("Digite seu nome completo: ")).strip()
print("O nome em maiusculo é {}".format(nome.upper()))
print("o nome em minusculas é {}".format(nome.lower()))
print("O total de caracteres do seu nome é {}".format(len(nome) - nome.count(" ")))
print("O total de letras do primeiro nome é {}".format(nome.find(" ")))
t = nome.upper().split()
print("O total de letras do primeiro nome é {} (funcçao dois)".format(len(t[0])))
x = nome.upper().rsplit(maxsplit=1)
print("O seu primeiro nome e seu sobrenome  '{} {}'".format(t[0], x[1]))

nome1 = nome.upper().split()
print("Outra forma é assim '{}'".format(nome1[-1]))
print("A terceira forma é asssim '{}'".format(nome1[len(nome1)-1]))

p = str(input("Qual nome vamos pesquisar?"))
p = p.upper()
print("A resposta para se o '{}' pertence ao nome é: \n{}".format(p, p in nome.lower()))

#encontrando a letra "a" Quantas? Posiçao da primeira? Posiçao da ultima?
q = nome.lower().count("a")
print("A quantidade de letras 'A' em seu texto é {}".format(q))

k = nome.lower().find("a")
k2 = nome.lower().rfind('a')
print("O primeiro 'A' fica na posiçao {}, o ultimo 'A' na posiçao {}".format(k+1, k2+1))
