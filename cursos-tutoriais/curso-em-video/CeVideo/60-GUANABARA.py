from math import factorial

numero = int(input("digite um numero: "))


f = 1
c = numero

while c > 0: 
    
    print(c, end=" ")
    print("x " if c > 1 else " = ", end="")
    f *= c
    c -= 1
    
print(f)
