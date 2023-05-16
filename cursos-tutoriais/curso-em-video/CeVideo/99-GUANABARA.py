from time import sleep


def maior(*n):
    cont = maior = 0
    print('-='*30)
    print('Analisando os valores passados')
    
    for valor in n:
        print(f'{valor}', end=' ', flush=True)
        sleep(0.3)
        
        if cont == 0:
            maior = valor
        else:
            
            if valor > maior:
                maior = valor
                
        cont += 1
        
        
    print(f'foram informados {cont} valores ao todo.')
    print(f' O maior valor informado foi {maior}.')



maior(1, 5, 4, 3, 2, 5, 6)
maior(4,7, 6, 4, 9, 43)
maior()