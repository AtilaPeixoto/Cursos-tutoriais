cor = ('\033[m',         # 0 limpa
       '\033[31m',       # 1 vermelho
       '\033[33m',       # 2 verde
       "\033[34m",       # 3 azul
       "\033[1m",        # 4 negrito
       '\033[7m')        # 5 inverte


def linha(tam=40):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(40))
    print(linha())


def menu(x):
    cont = 1
    print(linha())
    cabecalho(f'{cor[4]}MENU PRINCIPAL{cor[0]}')
    for i in x:
        print(f'{cor[3]}[{cont}] - {i}{cor[0]}')
        cont += 1
    print(linha())
    opc = leiaInt()
    return opc

def leiaInt():
    try:
        m = str(input(f'{cor[2]}Opção:  {cor[0]}'))
    except (ValueError, TypeError):
        print(f'{cor[1]}digite um opção valida{cor[0]}')
    except KeyboardInterrupt:
        print('programa encerrado pelo usuario')
        return 0
    else:
        return m



