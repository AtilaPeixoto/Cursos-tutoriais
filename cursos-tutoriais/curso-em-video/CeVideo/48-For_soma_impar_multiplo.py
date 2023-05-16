# soma impares multiplos de 3


s = 0
cont = 0
cont1 = 0

# lembre-se de por um numero extra para fechar a conta
for r in range(1, 501, 2):
    
    if r % 3 == 0:
        
        # o espaço fica entre cada numero
        print('\033[7m', r,'\033[m', end=" ")
        
        s = int(s + r)
        cont1 += 1
        
    cont += 1
    
    
# o end= emenda o print com o proximo, alem de organizar na horizoltal, entao é preciso um print vazio para quebrar a sequencia do end=''
print()

print(f"""O total de impares é {cont}
O total de impares multiplos de 3 é {cont1}
A soma dos mltiplos de 3 é {s}""")