n = float(input("Primeira medida"))
n2 = float(input("Segnda medida"))
n3 = float(input("Terceira medida"))

if (n + n2)< n3 or (n +n3) < n2 or (n2 + n3) < n:
    print("Estas medidas nao formam triangulo")
else:
    if n == n2 and n == n3 and n2 == n3:
        print("Triangulo equilatero")
    elif n != n2 and n != n3 and n2 != n3:
        print("Triangulo ESCALENO")
    else:
        print("triangulo ISOSCELES")