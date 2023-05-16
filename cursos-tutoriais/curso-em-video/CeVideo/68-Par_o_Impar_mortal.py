from random import randint




cont_vitoria_jogador = 0

while True:
    numero_jogador = int(input("Digite um numero Par ou Impar: "))
    
    if numero_jogador % 2 == 0:# definiçao do lado
        jogador = "PAR"
        pc = "IMPAR"
    else:
        jogador = "IMPAR"
        pc = "PAR"
        
    print(f"Voce escolheu {jogador} e o PC escolheu {pc}")
    
    numero_pc = randint(0, 3)
    print(f"PC escolheu ", numero_pc)
    
    if (numero_jogador + numero_pc) % 2 == 0:# definiçao do resultado
        resultado = "PAR"
    else:
        resultado = "IMPAR"
        
    if resultado == jogador:      # contador de vitorias com parada
        cont_vitoria_jogador += 1
        print(f"\033[1mVoce venceu com \033[7m{resultado}\033[m!")
    else:
        print(f"PC venceu com \033[7m{resultado}\033[m! \033[31mGAME OUVER!\033[m")
        break
    
    
print(f"\033[1:7mVoce venceu {cont_vitoria_jogador}")

