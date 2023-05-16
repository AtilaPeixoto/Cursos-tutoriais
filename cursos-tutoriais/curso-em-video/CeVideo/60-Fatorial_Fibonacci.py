z = ""
x = maior = menor = 0

while sair != "sair":

    opcao = str(input("""
    [1] FATORIAL
    [2] FIBONACCI
    [3] SOMA MEDIA E Maior e Menor
    SUA ESCOLHA: """))
    
    
    numero = int(input("Digite um numero para seguir: "))
    
    
    if opcao == "1":
        i = 2
        f = 1
        
        # o do guanabara mostra o um
        while i <= numero:
            f *= i
            i += 1
            print(f)
            
            
    elif opcao == "2":
        i = 0
        x = 0
        vezes = int(input("Qual sera o numero de vezes? "))
          
        while i <= vezes:
            f = numero + x
            x = numero
            numero = f
            i += 1
            print(f)
                     
                     
    elif opcao == "3":
        cont = x = s = 0
        x = int(input("add numero:"))
        
        while x != 999:
            s += x
            cont += 1
            
            if cont == 1:
                menor = x
                maior = x
            else:
                if x < menor:
                    menor = x
                    
                if x > maior and x!= 999:
                    maior = x
                    
            print("=="*20)
            print("\033[31m Para sair aperte \033[m \033[7m 999 \033[m")
            print("=="*20)
            
            x = int(input("add numero:"))
            
            
        media = (s) /cont
        
        print(f"""
        o maior numero: {maior}
        O menor numero: {menor}
        A media dos numeros: {media}
        A soma dos numeros: {s}
        """)
        
        
    sair = str(input("terminar?\033[7m Escreva 'SAIR'\033[m"))