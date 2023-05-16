notas = []
aluno = []
turma = []
media = e = 0
aluno_nome = add_mais_alunos = f = ""
print('-=-'*20)
print(f'\033[7m{" CADASTRO - NOTAS - BOLETIM ":*^50}\033[m')


while 'n' not in add_mais_alunos:
    print('-=-' * 20)
    aluno_nome = str(input('\033[1m Nome do aluno:\033[m ').upper().strip())
    aluno.append(aluno_nome)
   
    soma_notas = pos = 0
    for i in range(0, 2):
        pos += 1
        nota = float(input(f'Nota {pos} de {aluno_nome}:    '))
        soma_notas += nota
        media = soma_notas / 2
        notas.append(nota)
    
    
    aluno.append(notas[:])        
    aluno.append(media)
    turma.append(aluno[:])
    notas.clear()
    aluno.clear()
    
    add_mais_alunos = str(input('\033[31m Add outro?[S/N]\033[m ').lower().strip())

# resolvi deixar desta maneira para sempre lembrar o trabalho preciso para faer algumas funçoes com lista

# organizando alunos por ordem alfabetica
turma.sort()

# apresentando lista de alunos- aqui apresendado nome e medio
print('-=-'*20)
print(f'\033[1mAluno       Média\033[m')
for i in range(0, len(turma)):
    print(f'[{i+1}]{turma[i][0]:<10}{turma[i][2]:.>1}')

print('-=-'*20)

# olhando um individualmente - aqui apresentado notas detalhadas
while "n" not in f:
    e = int(input(f'\033[1mEscolha o aluno para ver individualmente:\033[m '))
    e -= 1
    print(f'Aluno: {turma[e][0]}\nNotas: {turma[e][1]}\nMedia: {turma[e][2]}')
    f = str(input(f'Terminar aperte - N - outra para voltar a Boletim ').lower())



