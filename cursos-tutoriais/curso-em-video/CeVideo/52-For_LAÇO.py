

while True:
    print(f'{" É PRIMO OU NÃO ":=^40}')
    print()
    numero = int(input("Digite um numero: "))

    total_par = 0
    total_impar = 0

    # o range engole o ultimo numero. Para mostrar o numero escolhido é preciso add mais um
    for i in range(1, numero +1):
        
        # A condicional seleciona a cor
        if numero % i == 0:
            print("\033[32m", end=" ")
            total_par += 1
        else:
            print("\033[31m", end=" ")
            total_impar += 1
        
        # printa os numeros    
        print(f"{i}\033[m", end=" ")
        
        
    print()
    print(f"""\033[32mNumeros em verde são as divisões do numero digitado.\033[m
        
    Numeros primos São divisiveis apenas duas vezes!

    \033[31m O numero degitado foi divisivel um total de {total_par} vezes \033[m""")
    
    
    # jogar novamente
    print()
    repetir = str(input(f'Tentar novamente?[S/N]:   ')).lower()
    if repetir == 'n':
        break