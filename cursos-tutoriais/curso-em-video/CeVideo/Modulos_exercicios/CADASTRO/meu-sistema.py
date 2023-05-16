from LIBI.INTERFACE import *
from LIBI.leiadoc import *


cabecalho(f'{cor[4]}{cor[5]}SISTEMA DE CADASTRO V1.0{cor[0]}')

while True:
    res = menu(['CADASTRAR NOVO', 'VER CADASTRO', 'SAIR'])
    
    if res == '1':
        cabecalho('Opção [1] Cadastrar')
        novo()
    elif res == '2':
        cabecalho('Opção [2] Ver Lista')
        ver()
    elif res == '3':
        cabecalho('Opção [3] Sair')
        break
    else:
        print(f'{cor[1]}Valor invalido{cor[0]}')

