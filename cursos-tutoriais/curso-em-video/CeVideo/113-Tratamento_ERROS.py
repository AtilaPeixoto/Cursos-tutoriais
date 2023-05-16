


def leiaint():
    while True:
        
        try:
            x = str(input('numero: '))
            int(x)
        except KeyboardInterrupt:
            print(' programa encerrado')
        except TypeError:
            print(' problema com o tpo de dados')
        except Exception as erro:
            print(f'O erro foi em {erro.__class__}')
        else:
            print(' o valor é um numero')
            break


def leiareal():
    while True:
        try:
            x = str(input(f'numero real:  ').replace(',', '.'))
            float(x)
        except ValueError:
            print(f' Valor incompativel')
        except KeyboardInterrupt:
            print('o programa foi encerrado')
        else:
            if '.' in x:
                print('o numero digitado é um numero real')
                break
            else:
                print(' o valor digitado é inteiro. Digite um numero real.')


leiaint()
leiareal()

# se liga que é possivel agora encerrar a primeira parte do programa
# sem afetar a segunda, por causa da KeyboardInterrpt