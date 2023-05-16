



tupla = ()
lista1 = {'DESCONTO 10%': 'x', 'ACRESCIMO 20%': 'x', 'Dobro': 'x'}
lista = []
dicionario = {}


def verint():
    """
    faz a leitura
    verifica se é int
    verifica se é float
    troca a virgula por ponto, caso ela exista
    :return: float(x)
    """
    while True:
        x = str(input('NUMERO:  ').strip())
        if x.isnumeric():   # função testa para int
            break
        else:
            f = veri(x)  # função testa para float
            if f:       # blood
                break
    x = put(x)          # função para trocar a virgula
    return x
# conforme o modelo do guanabara no exe 112 dava pra resoover apenas com o isnumeric()
# acho que acabei desenvolvendo tudo isso por um bag em outro setor do programa
# vou diar assim por ter esse cod do try  mas ocupa muuito menos espaço do outro jeito


# tava pensando que se eu retira-se a virgula/ponto temporariamente
# nao seria preciso testar para float mas voou deixar assim para aprendizado da função.
def veri(x):
    """
    esta porra retorna verdadeiro e falso apenas
    :param x: a ser testado
    :return: verdadeiro ou falso
    """
    if ',' in x:
        x = x.replace(',', '.')
    try:
        float(x)
        return True
    except ValueError:
        return False


def put(x):
    """
    troca a virgula por ponto, caso ela exista
    :param x: str a ser testada
    :return: x
    """

    if ',' in x:
        x = x.replace(',', '.')
    return x


def leiaDados(*x):
    """
    recebe os dados os poem em tupla
    os transfere para um dicionario com respectiva chave
    e os mostra em designer de tabela
    :param x: valores
    :return: tabela
    """
    tupla = x
    c = 1
# claramente a uma questao com escolha das formulas, caso queira escolher
    # funciona apenas caso todas sejam usadas ou claro com alteração no programa
    # add a chave
    for i in tupla:
        if c == 1:
            lista1['DESCONTO 10%'] = i
        elif c == 2:
            lista1['ACRESCIMO 20%'] = i
        elif c == 3:
            lista1['Dobro'] = i
        c += 1
    lista.append(lista1.copy())
    print('='*40)
    print(f'{"RECORENCIA":15}|{"VALOR":^10}')
    print('='*40)
    for i in lista:
        for k, v in i.items():
            print(f'{k:15}: {v}')



