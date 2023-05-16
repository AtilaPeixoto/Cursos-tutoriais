from datetime import date

agora = date.today()
ano = agora.year


nasc = int(input("Que ano nasceu o atleta? "))

print(ano)

idade = int(ano - nasc)
print(idade)


if idade <= 9:
    print("Categoria MIRIM")
elif idade > 9 and idade <= 14:
    print("Categoria JUNIOR")
elif idade > 14 and idade <= 19:
    print("Categoria JUVENIL")
else:
    idade >= 20
    print("Categoria SENIOR")
