ficha = [] # lista
aluno = {} # dicionario


for i in range(0, 3):
    # perceba a variavel é a posição no dicionario
    aluno['NOME'] = str(input('NOME: ').strip().upper()) 
    aluno['MEDIA'] = int(input('MEDIA: '))
    
    
    if aluno['MEDIA'] >= 7:
        aluno['AVALIAÇÃO'] = 'APROVADO'
    else:
        aluno['AVALIAÇÃO'] = 'REPROVADO'
        
    # com dicionarios é preciso usar o copy nao é posivel o- [:] fatiamento-    
    ficha.append(aluno.copy()) 
    
print('-='*20)
for i in ficha:   
    print('-='*20)
    # categoria e resposta c, v
    # .values() nao fumego, ainda nao sei o motivo/ tudo certo fora isso
    for c, v in i.items():  
        print(F'{c:<10}: {v:>10}')
