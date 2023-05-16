

frase = input("Digite uma palavra ou frase: ")


a = "".join(frase.split())

inverso = ""

# para cada em temanho de... de tras contar_regressivo saltando_um
for i in range(len(a) -1, -1, -1):
    inverso += a[i]
    
    print(inverso)
print()

if inverso != a:
    print("\033[31mNão é Palindromo \033[m")
else:
   print("\033[33mPalindormo\033[m")

