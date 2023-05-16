cor = {'vermelho': '\033[31m',
       'verde': '\033[32m',
       'branco': '\033[7m',
       'azul': '\033[33m',
       'limpa': '\033[m'}

fim = ""

while fim != "6":
    print("==="*20)
    
    numero = int(input("Digite o primeiro numero: "))
    numero_segundo = int(input("Digite o seguno numero: "))
    
    print("-=-"*20)
    print(f"{'vamos jogar':=^20}")
    
    opcao = str(input("""
    [1] SOMAR5
    [2] DIVIDIR
    [3] MULTIPLICAR
    [4] FIBONACCI
    [5] MAIOR E MENOR 
    [6] SAIR
    Sua escolha: """))



    if opcao == '1':
        soma = numero + numero_segundo
        print("A soma é: ", soma)
        
    elif opcao == "2":
        d = numero / numero_segundo
        print("A divisao é: ", d)
        
    elif opcao == "3":
        m = numero * numero_segundo
        print("A mutiplicaçao é: ", m)
    elif opcao == "4":
        n3 = numero
        print(cor["branco"], numero, cor["limpa"], end=" ")
        
        for i in range(0, numero_segundo):
            fibonacci = numero + n3
            numero = n3
            n3 = fibonacci
            print(cor["branco"], fibonacci, cor["limpa"], end=" ")
            
        print()

    elif opcao == "5":
        
        if numero > numero_segundo:
            mx = numero
            mm = numero_segundo
        else:
            mx = numero_segundo
            mm = numero
            
        print(f"O maior é {cor['verde']}{mx}{cor['limpa']} e o menor é {cor['azul']}{mm}{cor['limpa']}")
    
    
    elif opcao == "6":
        fim = "6"
    else:
        print(f"\033[31m Opçao invalida \033[m ")
        