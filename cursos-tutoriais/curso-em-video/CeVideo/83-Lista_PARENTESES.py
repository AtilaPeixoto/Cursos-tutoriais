# a grande jogada deste exeercicio é que a lista deve terminar vazia
# para cada um posto deve haver um retirado. atentar que os ) fechando nao sao inclusos mas retiramos um
# que abre ( para cada fechando )

minha_lista = []

expressao = str(input('Digite uma expressao :'))


for simbulo in expressao:

    if simbulo == '(':
        minha_lista.append('(')
    elif simbulo ==')':


# quando tem m fechando ) vem pra ca e tiramos um abrindo (
        if len(minha_lista) > 0:
            minha_lista.pop()
        else:
            minha_lista.append(')')
            break


# se houver algum indice na lista a expressao esta errada        
print(minha_lista)       
if len(minha_lista) > 0:          
    print('expressao errada')

