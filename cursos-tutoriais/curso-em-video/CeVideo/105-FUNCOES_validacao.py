notas = []
alunos = {}
turma = []


def media(*p, sit=False):
    """
    CALCULA A MEDIA E AVALIA A SITUAÇÃO
    :param p: sao as notas
    :param sit: situação conforme media
    :return: retorna a media
    """
    
    for indice in range(0, len(notas)):
        m = sum(p[indice]) / len(notas)
        
        if sit:
            if m > 7:
                alunos['SITUAÇÃO'] = 'APROVADO'
            elif m >= 5:
                alunos['SITUAÇÃO'] = 'RECUERÇÃO'
            else:
                alunos['SITUAÇÃO'] = 'REPROVADO'
        return m


for x in range(0, 2):
    alunos.clear()
    notas.clear()
    
    while True:
        a = str(input('\033[7mNOME:    \033[m'))
        
        if a != "":
            break
        
    alunos['NOME'] = a
    
    for i in range(0, 4):
        while True:
            n = str(input('NOTA:    '))
            
            if n.isnumeric():
                n = int(n)
                notas.append(n)
                alunos['NOTAS'] = notas[:]
                break
            
            
    alunos['MEDIA'] = media(notas, sit=True)
    alunos['MENOR NOTA'] = min(notas)
    alunos['MAIOR NOTA'] = max(notas)
    turma.append(alunos.copy())
    
    
for i in turma:
    print('='*30)
    
    for k, v in i.items():
        print(f'{k:<12}:{v}')
