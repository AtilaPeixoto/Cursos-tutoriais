'''PARA COISASA QUE SE REPETEM MUITO É BOM CRIAR ROTINAS
FUNÇOES SAO ROTINAS- PARA ROTINAS-.
'''

def lin():
    print('-'*20)

lin()
print('curso em video')
lin()
####################################3
def mensagem(msg):
    print('-'*20)
    print(msg)
    print('-'*20)

mensagem('sdsd')
####################################3
def titulo(txt):
    print('-'*20)
    print(txt)
    print('-'*20)

titulo('curso')
####################################3
'''exemplos
repetiçoes de função soma'''
a = 4
b = 5
s = a + b
print(s)

a= 8
b = 9
s = a + b
print(s)
'''
repetitivo? criar função'''
def soma(a, b):
    s = a + b
    print('função', s)
soma(4, 5)
soma(8, 9)
soma(b=8, a=9)# é possive escolher, caso nao o sistema passara por referencia.
# caso escoler uma, escolher todas! nao é possivel tornar explicito apenas uma.

'''mais um dos grandes diferenciaes do python em relaçao a outras linguagens reconheer 
 a passagem de parametro, forma conheida como EMPACOTAMENTO . segue exempo '''
def cont(*num):# o asterisco significa DESEMPAOTAR- jogar dentro de 'num' quantos forem os parametros
    for x in num:
         print('função com *', x, end=' ') # por a geração aqui ser uma tupla, apenas coisas de tuplas é possivel.
    print()
cont(5, 3)
cont(9, 8, 6)# sim claro, parentes sao tuplas ////
cont(3, 5, 1, 6, 8)
# o resultado é uma tupla


def dobra(lst):            # recebe a lista, a fnçao dobra
    pos = 0                 # criada para contar o tamho da lista e acompanha-la
    while pos < len(lst):
        lst[pos] *= 2       # variavel da posição recebe ela msm *2
        pos += 1


valores = [7, 6, 3, 2, 1]
print('lista normal', valores)
dobra(valores)      # chama a função porem como nao ha comando print na funçao é preciso um fora
print('posterior a função', valores)

'''
diferente de outras linguagens como o java one a passagem de parametro é por valor, no python é por referencia.
tudo que for feito na funçao vai interferir na lista valores diretamente.
'''
# para desempacotar
def soma2(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'SOMA2 - DESEMPACOTAR -somando os valores {valores} temos {s}')

soma2(4, 5)
soma2(3, 5, 4, 7)
