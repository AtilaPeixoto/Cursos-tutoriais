


minha_lista = []
fim = ''

# while True:
while 'n' not in fim:
    quantia_numeros = int(input(' quantos numeros serão add?'))       

    if quantia_numeros == 0:                                          
        break

    for i in range(0, quantia_numeros):                               
        numero = int(input('digite um numero '))

        if numero in minha_lista:
            print('ja existente ')
        else:
            minha_lista.append(numero)
            
    fim = str(input('Continuar?[S/N] ')).lower()             

    # if fim == "n":
    #     break
    
print(minha_lista)
