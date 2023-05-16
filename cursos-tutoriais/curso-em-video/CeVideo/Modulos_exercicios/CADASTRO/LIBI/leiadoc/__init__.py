def novo():
    n = str(input('Nome: ').upper())
    i = str(input('Idade: '))
    with open(fr'{"meu-cadastro"}', 'a') as f:
        cad = f.write(f'{n};{i}\n')


    

def ver():
    with open(fr'{"arquivo"}', 'r') as f:
        for i in f:
            dado = i.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
