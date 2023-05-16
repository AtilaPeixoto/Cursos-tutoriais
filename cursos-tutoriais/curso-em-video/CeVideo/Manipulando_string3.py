a ="aprendendo python"
b =len(a)
b2 = a[::-1]
c = a.count("a", 0, 9)
# miusculas e minusculas nao sao a mesma coisa
d = a.find("end")
# maiusculas e minusculas nao sao a mesma coisa, nunca
e = a.upper()
f = a.lower()
g = a.strip()
#remove espaços no inicio e no final
g1 = a.lstrip()
#remove na esquerda left
g2 = a.rstrip()
# remove right
h = a.split()
# separador de palavras/ no uso do len cada palavra seria uma cadeia de caracter
i = a.title()
j = a.replace("python", "a viver")
h1 = "_".join(a)
h2 = "*".join(a)
h3 = "".join(a.split())

print("a) ",a)
print("b) ", b)
print("b2) ", b2) # escrevendo de tras para frente -- palindromo -use h3 para retirar espaços
print("c) ", c)
print("d) ", d)
print("e) ", e)
print("f) ", f)
print("g's", g, g1, g2)
print("h) ", h)
print("h1) ", h1)
print("i) ", i)
print("j) ", j)
print("h2) ", h2)
print("h3) ", h3)

div = a.split()
print("A segunda palavra é '{}' ".format(div[0]))
# a prieira palavra é 0
print("A quarta letra da segunda palavra é '{}' ".format(div[1][3]))
#palavra e posiçao
print("O loca da palavra é {}".format(a.lower().find("python")))
#tranformei em minusculo e mandei procurar
#verificando qual posiçao (letra inicial)
print("aprendendo" in a)
# verificando se existe em
print("""Desta maneira com tres aspas é possivel escrever um texto bom grande
em varias linhas usando apenas um comando print""")



