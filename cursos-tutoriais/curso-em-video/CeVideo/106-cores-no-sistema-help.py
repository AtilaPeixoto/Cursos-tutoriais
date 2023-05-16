from time import sleep
cor = ('\033[m',        # limpa
       '\033[0;30;41m', # vermelho
       '\033[45m',      # roxo
       '\033[44m'       #azul
       )

# busca no help
def ajuda(x):
    titulo(f'ACESSANDO O MANUA DO COMANDO \'{x}\' ', 2)
    print(cor[3], end='')
    help(x)
    print(cor[0], end='')
    sleep(2)

# efeito de cores e desenhos
def titulo(msg, c):
    tam = len(msg)+4
    print(cor[c], end='')
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)
    print(cor[0], end=' ')
    sleep(1)


#programa principal
while True:
    titulo('SIS DE AJUDA DO PyHelp', 1)
    a = str(input('QUAL BIBLIOTECA OU FUÇÃO?'))
    
    if a.upper() == 'FIM':
        break
    else:
        ajuda(a)
titulo('ATÉ LOGO!!!', 1)