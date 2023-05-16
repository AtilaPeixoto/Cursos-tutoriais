


def cond(x):
    from datetime import date   # primeira importação dentro de função
    ano = date.today().year
    
    i = ano - nasc                   
    if 16 <= i < 18 or i > 65:
        return ' FACULTATIVO'
    elif i < 16:
        return '\033[31nNAO AUTORIZADO\033[m'
    else:
        return 'OBRIGATORIO'


nasc = int(input('Ano de nascimento: '))
print(cond(nasc))
